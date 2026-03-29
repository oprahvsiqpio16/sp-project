export default async function handler(req, res) {
    if (req.method === 'POST') {
        const { message } = req.body;
        
        const BOT_TOKEN = "8713127522:AAGfj4acg204MMc0SX7keJNtP4fWN9L-lYQ";
        const CHAT_ID = "7984067238";

        const telegramUrl = `https://api.telegram.org/bot${BOT_TOKEN}/sendMessage`;

        try {
            await fetch(telegramUrl, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    chat_id: CHAT_ID,
                    text: message, // النص المنسق القادم من الواجهة
                    parse_mode: "Markdown" // لتفعيل الخط العريض والرموز
                })
            });
            return res.status(200).json({ success: true });
        } catch (error) {
            return res.status(500).json({ error: error.message });
        }
    }
    res.status(405).json({ message: 'Method not allowed' });
}
