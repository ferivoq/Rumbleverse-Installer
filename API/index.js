const express = require('express');
const cors = require('cors');
const fs = require('fs');
const path = require('path');

const app = express();
app.use(cors());

const getVersionsData = () => {
    const versionsDirectory = path.join(__dirname, 'versions');
    const files = fs.readdirSync(versionsDirectory);

    return files
        .filter(file => file.endsWith('.zip'))
        .map(file => {
            const name = file.replace('.zip', '');
            return {
                name: name,
                link: `https://rvapi.ferivoq.me/versions/${encodeURIComponent(file)}`
            };
        });
};

app.use('/versions', express.static(path.join(__dirname, 'versions')));

app.get('/api', (req, res) => {
    const data = { versions: getVersionsData() };
    res.json(data);
});

app.get('/', (req, res) => {
    res.send('Rumbleverse Download API');
});

const PORT = 4000;
app.listen(PORT, () => {
    console.log(`Server is running on port http://localhost:${PORT}`);
});
