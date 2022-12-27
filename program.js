// 120
// 240
// 360
// 480
// 600

const fs = require("fs");
const Jimp = require("jimp");

Jimp.read("test3.jpg", (err, image) => {
  for (let i = 120; i < 640; i = i + 120) {
    let pixArr = [];
    console.log(i)
    for (let j = 100; j < 120; j++) {
      pixArr.push(Jimp.intToRGBA(image.getPixelColour(j, i)));
    }
    console.log(pixArr);
  }
});

// "test"
// [
//   { r: 57, g: 20, b: 23, a: 255 },
//   { r: 56, g: 22, b: 24, a: 255 },
//   { r: 52, g: 22, b: 20, a: 255 },
//   { r: 50, g: 23, b: 18, a: 255 },
//   { r: 60, g: 20, b: 19, a: 255 },
//   { r: 49, g: 16, b: 13, a: 255 },
//   { r: 46, g: 16, b: 12, a: 255 },
//   { r: 60, g: 27, b: 24, a: 255 },
//   { r: 49, g: 12, b: 15, a: 255 },
//   { r: 63, g: 35, b: 36, a: 255 },
//   { r: 75, g: 65, b: 64, a: 255 },
//   { r: 165, g: 172, b: 168, a: 255 },
//   { r: 146, g: 146, b: 146, a: 255 },
//   { r: 166, g: 166, b: 166, a: 255 },
//   { r: 164, g: 164, b: 164, a: 255 },
//   { r: 146, g: 146, b: 146, a: 255 },
//   { r: 202, g: 202, b: 202, a: 255 },
//   { r: 139, g: 139, b: 139, a: 255 },
//   { r: 43, g: 43, b: 43, a: 255 },
//   { r: 36, g: 36, b: 36, a: 255 }
// ]
