let current_version = 0.3;

let languageTranslation = {
  en: {
    title: "Title",
    category: "Category",
    notes: "Notes"
  },

  zh: {
    title: "标题",
    category: "类别",
    notes: "笔记"
  }
};
let languageCode = navigator.language.substr(0, 2);
let language = languageTranslation[languageCode]
export default language;
