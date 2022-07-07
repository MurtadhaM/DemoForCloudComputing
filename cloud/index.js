// Import the functions you need from the SDKs you need

import { initializeApp } from "firebase/app";

import { getAnalytics } from "firebase/analytics";

// TODO: Add SDKs for Firebase products that you want to use

// https://firebase.google.com/docs/web/setup#available-libraries


// Your web app's Firebase configuration

// For Firebase JS SDK v7.20.0 and later, measurementId is optional

const firebaseConfig = {

  apiKey: "AIzaSyBTPKjE7WAMxojFVD1YGKaDCRaxTTXtMGQ",

  authDomain: "wellnecity-monitor.firebaseapp.com",

  projectId: "wellnecity-monitor",

  storageBucket: "wellnecity-monitor.appspot.com",

  messagingSenderId: "848464238736",

  appId: "1:848464238736:web:41624e2d1c5dd681b82015",

  measurementId: "G-34NCW374CR"

};


// Initialize Firebase

const app = initializeApp(firebaseConfig);

const analytics = getAnalytics(app);
