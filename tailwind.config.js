/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      scale: {
        '101': '1.01',
        '102': '1.02',
        '103': '1.03',
        '104': '1.04'
      }
    }
  },
  plugins: [],
}
