const fs = require('fs');

// destination will be created or overwritten by default.
fs.copyFile('C:\fakepath\big_data.jpg', 'C:\folderB\myfile.txt', (err) => {
  if (err) throw err;
  console.log('File was copied to destination');
});