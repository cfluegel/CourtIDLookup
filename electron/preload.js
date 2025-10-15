const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
  loadDataset: (relativePath) => ipcRenderer.invoke('load-dataset', relativePath)
});
