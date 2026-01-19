
import { Note, NoteCreate } from '../types';

const BASE_URL = import.meta.env.VITE_API_BASE_URL || 'https://api.andrey.qix.ee';

export const api = {
  async listNotes(): Promise<Note[]> {
    try {
      const response = await fetch(`${BASE_URL}/notes/`);
      if (!response.ok) {
        const text = await response.text();
        throw new Error(`Failed to fetch notes: ${response.status} ${text}`);
      }
      return response.json();
    } catch (error) {
      console.error('API Error (listNotes):', error);
      throw error;
    }
  },

  async getNote(id: string): Promise<Note> {
    try {
      const response = await fetch(`${BASE_URL}/notes/${id}`);
      if (!response.ok) throw new Error('Failed to fetch note');
      return response.json();
    } catch (error) {
      console.error('API Error (getNote):', error);
      throw error;
    }
  },

  async createNote(note: NoteCreate): Promise<Note> {
    try {
      // The OpenAPI spec implies POST /notes/ for creation
      const response = await fetch(`${BASE_URL}/notes/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(note),
      });
      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail?.[0]?.msg || 'Failed to create note');
      }
      return response.json();
    } catch (error) {
      console.error('API Error (createNote):', error);
      throw error;
    }
  },

  async updateNote(id: string, note: NoteCreate): Promise<Note> {
    try {
      const response = await fetch(`${BASE_URL}/notes/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          ...note,
          id: id,
          created_at: new Date().toISOString() // API schema expects full Note object for PUT
        }),
      });
      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail?.[0]?.msg || 'Failed to update note');
      }
      return response.json();
    } catch (error) {
      console.error('API Error (updateNote):', error);
      throw error;
    }
  },

  async deleteNote(id: string): Promise<void> {
    try {
      const response = await fetch(`${BASE_URL}/notes/${id}`, {
        method: 'DELETE',
      });
      if (!response.ok) throw new Error('Failed to delete note');
    } catch (error) {
      console.error('API Error (deleteNote):', error);
      throw error;
    }
  }
};
