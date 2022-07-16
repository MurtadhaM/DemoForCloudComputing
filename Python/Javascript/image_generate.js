
import fetch from 'node-fetch';
const fs = require('fs');

async function image_generate(url) {
    const response = await fetch(url);
    return response

}



var data = fs.writeFileSync('image.png', image_generate('https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png'));


