
import { GoogleGenAI } from "@google/genai";

export const summarizeNote = async (content: string): Promise<string> => {
  if (!content || content.length < 50) return "Note is too short to summarize.";
  
  try {
    const ai = new GoogleGenAI({ apiKey: process.env.API_KEY });
    const response = await ai.models.generateContent({
      model: 'gemini-3-flash-preview',
      contents: `Summarize the following note in one concise sentence: "${content}"`,
    });
    return response.text || "Could not generate summary.";
  } catch (error) {
    console.error("Gemini Error:", error);
    return "AI summarization unavailable.";
  }
};
