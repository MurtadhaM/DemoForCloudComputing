const express = require('express')

// Create a new express application instance
const app = express();





// A a route handler for the default home page
app.get('/',  (req, res) => {
    res.redirect('/Home')
}
);


app.get('/Home',  (req, res) => {
    // Handle the get request for the home page
    res.send('Home Page');
}
);

app.get('/Login',  (req, res) => {
    // Handle the get request for the Login
    res.send('Login Page');
}
);


app.get('/Register',  (req, res) => {
    // Handle the get request for the Login
    res.send('Registration Page');
}
);

app.get('/About',  (req, res) => {
    // Handle the get request for About Login
    res.send('About Page');
}
);


// start the server
app.listen(8080, () => {
    console.log('Server is running on port 8080');
    }
);