
import React, { useState, useEffect, useCallback } from 'react';
import { Note, NoteCreate } from './types';
import { api } from './services/api';
import { summarizeNote } from './services/gemini';
import { Toaster, toast } from 'sonner';

// Helper components defined outside to avoid re-renders
const SidebarItem: React.FC<{
  note: Note;
  isActive: boolean;
  onClick: () => void
}> = ({ note, isActive, onClick }) => (
  <button
    onClick={onClick}
    className={`w-full text-left p-4 transition-all duration-200 border-b border-slate-100 ${isActive
      ? 'bg-blue-50 border-r-4 border-r-blue-500'
      : 'hover:bg-slate-50'
      }`}
  >
    <h3 className="font-semibold text-slate-800 truncate">{note.title || 'Untitled Note'}</h3>
    <p className="text-sm text-slate-500 truncate mt-1">{note.content || 'No content...'}</p>
    <span className="text-[10px] text-slate-400 mt-2 block">
      {new Date(note.created_at).toLocaleDateString()}
    </span>
  </button>
);

const App: React.FC = () => {
  const [notes, setNotes] = useState<Note[]>([]);
  const [selectedNoteId, setSelectedNoteId] = useState<string | null>(null);
  const [editingNote, setEditingNote] = useState<NoteCreate>({ title: '', content: '' });
  const [isLoading, setIsLoading] = useState(false);
  const [isSaving, setIsSaving] = useState(false);
  const [aiSummary, setAiSummary] = useState<string | null>(null);

  const fetchNotes = useCallback(async () => {
    setIsLoading(true);
    try {
      const data = await api.listNotes();
      setNotes(data);
    } catch (error) {
      console.error(error);
      alert('Error fetching notes');
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchNotes();
  }, [fetchNotes]);

  const handleSelectNote = (note: Note) => {
    setSelectedNoteId(note.id);
    setEditingNote({ title: note.title, content: note.content });
    setAiSummary(null);
  };

  const handleNewNote = () => {
    setSelectedNoteId(null);
    setEditingNote({ title: '', content: '' });
    setAiSummary(null);
  };

  const handleSave = async () => {
    if (!editingNote.title.trim()) {
      alert('Please enter a title');
      return;
    }

    setIsSaving(true);
    try {
      if (selectedNoteId) {
        const updated = await api.updateNote(selectedNoteId, editingNote);
        setNotes(prev => prev.map(n => n.id === selectedNoteId ? updated : n));
      } else {
        const created = await api.createNote(editingNote);
        setNotes(prev => [created, ...prev]);
        setSelectedNoteId(created.id);
      }
    } catch (error) {
      console.error(error);
      alert('Error saving note');
    } finally {
      setIsSaving(false);
    }
  };

  const handleDelete = () => {
    if (!selectedNoteId) return;

    const noteToDelete = notes.find(n => n.id === selectedNoteId);
    if (!noteToDelete) return;

    const idToDelete = selectedNoteId;

    // Optimistically remove from UI
    setNotes(prev => prev.filter(n => n.id !== idToDelete));
    handleNewNote();

    let isUndone = false;
    let isProcessed = false;

    const finalizeDeletion = async () => {
      if (isUndone || isProcessed) return;
      isProcessed = true;
      try {
        await api.deleteNote(idToDelete);
      } catch (error) {
        console.error(error);
        toast.error("Failed to sync deletion");
        fetchNotes(); // Refresh to restore if sync failed
      }
    };

    // Show toast with undo action
    toast.error("Note deleted", {
      duration: 2000,
      description: `"${noteToDelete.title || 'Untitled Note'}" has been removed.`,
      action: {
        label: "Undo",
        onClick: () => {
          isUndone = true;
          setNotes(prev => [noteToDelete, ...prev]);
          setSelectedNoteId(idToDelete);
          setEditingNote({ title: noteToDelete.title, content: noteToDelete.content });
        },
      },
      onAutoClose: finalizeDeletion,
      onDismiss: finalizeDeletion,
    });
  };

  const handleAiSummarize = async () => {
    if (!editingNote.content) return;
    setAiSummary("Thinking...");
    const summary = await summarizeNote(editingNote.content);
    setAiSummary(summary);
  };

  return (
    <div className="flex h-screen bg-white overflow-hidden">
      <Toaster
        position="bottom-right"
        richColors
        theme="light"
        toastOptions={{
          className: 'shadow-lg border-slate-200',
          style: { borderRadius: '12px' }
        }}
      />
      {/* Sidebar */}
      <aside className="w-80 border-r border-slate-200 flex flex-col bg-slate-50">
        <div className="p-6 border-b border-slate-200 bg-white">
          <div className="flex items-center justify-between mb-4">
            <h1 className="text-xl font-bold text-slate-800 flex items-center gap-2">
              <span className="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center text-white text-lg">N</span>
              NoteFlow
            </h1>
          </div>
          <button
            onClick={handleNewNote}
            className="w-full py-2 px-4 bg-blue-600 hover:bg-blue-700 text-white rounded-lg font-medium transition-colors flex items-center justify-center gap-2 shadow-sm"
          >
            <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
              <path fillRule="evenodd" d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z" clipRule="evenodd" />
            </svg>
            New Note
          </button>
        </div>

        <div className="flex-1 overflow-y-auto custom-scrollbar">
          {isLoading ? (
            <div className="p-10 text-center text-slate-400">Loading...</div>
          ) : notes.length === 0 ? (
            <div className="p-10 text-center text-slate-400">No notes yet</div>
          ) : (
            notes.map(note => (
              <SidebarItem
                key={note.id}
                note={note}
                isActive={selectedNoteId === note.id}
                onClick={() => handleSelectNote(note)}
              />
            ))
          )}
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 flex flex-col bg-white">
        {/* Toolbar */}
        <header className="h-16 border-b border-slate-200 px-8 flex items-center justify-between sticky top-0 bg-white z-10">
          <div className="text-sm text-slate-400">
            {selectedNoteId ? `Editing existing note` : 'Creating new note'}
          </div>
          <div className="flex items-center gap-3">
            {selectedNoteId && (
              <>
                <button
                  onClick={handleAiSummarize}
                  className="px-4 py-2 text-slate-600 hover:bg-slate-100 rounded-lg text-sm font-medium transition-colors border border-slate-200 flex items-center gap-2"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-purple-500" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M17.414 2.586a2 2 0 00-2.828 0L7 10.172V13h2.828l7.586-7.586a2 2 0 000-2.828z" />
                    <path fillRule="evenodd" d="M2 6a2 2 0 012-2h4a1 1 0 010 2H4v10h10v-4a1 1 0 112 0v4a2 2 0 01-2 2H4a2 2 0 01-2-2V6z" clipRule="evenodd" />
                  </svg>
                  Magic Summary
                </button>
                <button
                  onClick={handleDelete}
                  className="px-4 py-2 text-red-600 hover:bg-red-50 rounded-lg text-sm font-medium transition-colors"
                >
                  Delete
                </button>
              </>
            )}
            <button
              onClick={handleSave}
              disabled={isSaving}
              className={`px-6 py-2 bg-slate-900 hover:bg-slate-800 text-white rounded-lg text-sm font-semibold transition-all shadow-md ${isSaving ? 'opacity-50 cursor-not-allowed' : ''}`}
            >
              {isSaving ? 'Saving...' : 'Save Changes'}
            </button>
          </div>
        </header>

        {/* Editor Area */}
        <div className="flex-1 p-8 md:p-12 max-w-4xl mx-auto w-full flex flex-col gap-6 overflow-y-auto custom-scrollbar">
          {aiSummary && (
            <div className="p-4 bg-purple-50 border border-purple-100 rounded-xl text-sm text-purple-800 animate-in fade-in slide-in-from-top-2 duration-300">
              <span className="font-bold uppercase text-[10px] tracking-wider block mb-1 opacity-60">AI Summary</span>
              {aiSummary}
            </div>
          )}

          <input
            type="text"
            placeholder="Note Title"
            value={editingNote.title}
            onChange={(e) => setEditingNote(prev => ({ ...prev, title: e.target.value }))}
            className="text-4xl font-bold text-slate-900 placeholder:text-slate-200 outline-none border-none bg-transparent"
          />

          <textarea
            placeholder="Start writing your thoughts..."
            value={editingNote.content}
            onChange={(e) => setEditingNote(prev => ({ ...prev, content: e.target.value }))}
            className="flex-1 text-lg text-slate-700 placeholder:text-slate-300 outline-none border-none bg-transparent resize-none leading-relaxed min-h-[400px]"
          />
        </div>

        {/* Floating footer for mobile (optional context) */}
        <footer className="md:hidden border-t border-slate-200 p-4 bg-white sticky bottom-0 flex justify-end">
          <button
            onClick={handleSave}
            className="px-8 py-3 bg-blue-600 text-white rounded-full font-bold shadow-lg"
          >
            Save
          </button>
        </footer>
      </main>
    </div>
  );
};

export default App;
