import type { ContentResponse } from "@/types";
import apiClient from "./apiClient";


export const fetchContent = async (): Promise<ContentResponse> => {
  try {
    return await apiClient.get<ContentResponse>('/api/content/');
  } catch (error) {
    console.error('Error fetching content:', error);
    throw error;
  }
};
