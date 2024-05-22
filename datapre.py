# const {Firestore} = require('@google-cloud/firestore');
# const express = require('express');
# const session = require('express-session');
# const app = express();
# const {initializeApp} = require("firebase/app")

# const {FirestoreStore} = require('@google-cloud/connect-firestore');

# // Initialize Firebase
# const firebaseConfig = {
#   apiKey: "AIzaSyCLPuCv0C4CdwcamS0Yz_FPZZV8CWp_BKs",
#   authDomain: "starlit-fire-413809.firebaseapp.com",
#   projectId: "starlit-fire-413809",
#   storageBucket: "starlit-fire-413809.appspot.com",
#   messagingSenderId: "743741808194",
#   appId: "1:743741808194:web:53b93154751e26036f57db"
# };
# initializeApp(firebaseConfig);

# // Create a new Firestore client
# const db = new Firestore({
#   projectId: firebaseConfig.projectId,
#   keyFilename: './saKey.json',
#   databaseId: "mom-summary"
# });


# const getCollection = (collection) => {
#   return db.collection(collection).get()
#     .then(res => {
#       return res.docs.map(doc => ({ id: doc.id, data: doc.data() }));
#     })
#     .catch(err => {
#       throw err;
#     });
# };

# const storeData = async (collection, data) => {
#   try {
#     const docRef = await db.collection(collection).add(data);
#     return docRef.id;
#   } catch (error) {
#     throw error;
#   }
# };

# const data = {
#   Description:"Mehta Chakka",
#   Title:"Manan Ko fifa nahi ata",
#   Calendarid:"test",
#   startTime: "Mar 14, 2024, 4:44:06.316 PM",
#   EndTime:"Mar 14, 2024, 4:45:06.316 PM"
# };

# storeData('app-script', data)
#   .then(docId => {
#     console.log(Data stored successfully with document ID: ${docId});
#   })
#   .catch(err => {
#     console.log(err);
#   });