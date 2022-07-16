const express = require('express'); 
const app = express();



 //setup the server
app.listen(3000, () => {
    console.log('Server is running on port 3000');
}
);


// setup the routes
app.get('/', (req, res) => {
    res.send('Hello World');
}
);


// API routes
app.get('/api/snake', (req, res) => {
    res.json(
   
        {
            id: 1,
            name: 'Snake',
            species: 'Python',
            length: '5m'

        } 

    ); 

}   
);




// setup /snake
app.get('/snake', (req, res) => {
    if(req.query.name) {
        res.send(`Hello ${req.query.name}`);
    } else {
    res.send('Snake is not named');
    }
}
);
