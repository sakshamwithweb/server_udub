import express from 'express'
const app = express()
const port = 3000

app.use(express.json());


app.get('/', (req, res) => {
    res.send('Hello There! This is Saksham workspace for UDUB')
})

app.post('/generate', async (req, res) => {
    try {
        res.status(200).json({ message: 'Processing completed.' });
    } catch (error) {
        console.error('Error in step1:', error);
        res.status(500).json({ error: 'An error occurred while processing.' });
    }
});



app.listen(port, () => {
    console.log(`Server is listening on port http://localhost:${port}`)
})
