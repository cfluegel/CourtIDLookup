const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('node:path');
const fs = require('node:fs/promises');

async function createWindow() {
  const mainWindow = new BrowserWindow({
    width: 1024,
    height: 768,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js')
    }
  });

  await mainWindow.loadFile(path.join(app.getAppPath(), 'index.html'));
  mainWindow.setMenuBarVisibility(false);
}

async function resolveDataset(_event, relativePath) {
  const datasetPath = path.join(app.getAppPath(), relativePath);
  const rawContent = await fs.readFile(datasetPath, 'utf-8');
  return JSON.parse(rawContent);
}

app.whenReady().then(() => {
  ipcMain.handle('load-dataset', resolveDataset);
  createWindow();

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});
