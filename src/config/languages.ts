export const LANGUAGES = [
  { code: "en", label: "English", htmlLang: "en", active: true },
  { code: "ja", label: "日本語", htmlLang: "ja", active: true },
  { code: "vi", label: "Tiếng Việt", htmlLang: "vi", active: false },
  { code: "id", label: "Bahasa Indonesia", htmlLang: "id", active: false },
  { code: "pt", label: "Português", htmlLang: "pt", active: false },
  { code: "th", label: "ไทย", htmlLang: "th", active: false },
  { code: "zh-TW", label: "繁體中文", htmlLang: "zh-TW", active: false },
] as const;

export type LanguageCode = (typeof LANGUAGES)[number]["code"];

export const ACTIVE_LANGUAGES = LANGUAGES.filter(l => l.active);

export const ACTIVE_LANGUAGE_CODES = ACTIVE_LANGUAGES.map(l => l.code);

export const DEFAULT_LANGUAGE: LanguageCode = "en";

export function isValidLanguage(code: string): code is LanguageCode {
  return LANGUAGES.some(l => l.code === code);
}

export function isActiveLanguage(code: string): boolean {
  return ACTIVE_LANGUAGES.some(l => l.code === code);
}

export function getLanguageLabel(code: string): string {
  return LANGUAGES.find(l => l.code === code)?.label ?? code;
}
