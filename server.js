// サーバー稼働テスト用のコードです
const express = require("express");

const app = express();
const PORT = 3000;

app.get("/", (req, res) => {
  res.send("サーバー稼働中\n");
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});