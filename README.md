# TUM Course Scraper: Automate Your Elective Search

## Overview
Finding the right elective courses at Technische Universität München (TUM) can be tedious, especially when dealing with dozens of options and needing to manually extract important details like **Semesterwochenstunden (SWS)**. This script automates that process, saving you time and effort.

### **Why Does SWS Matter?**
SWS represents the **weekly time commitment** for a course. If you're under **time pressure** and need an **easy elective** that offers the **most ECTS for the least SWS**, this tool will help you identify the best options. It also determines whether a course has a **written exam**, which can be crucial when planning your semester workload.

## **How It Works**
The script performs the following steps:
1. Uses **Google Search** to find the official course page on **campus.tum.de**.
2. Scrapes the page to extract **SWS** and checks whether an **exam is required**.
3. Returns one of three possible results:
   - `[COURSE_ID] No Exam | SWS: X`
   - `[COURSE_ID] Exam | SWS: X`
   - `[COURSE_ID] No result found.` (if Google blocks scraping or the course page isn't found)

## **Google Scraping Constraints**
Since TUM does not provide a public API for course data, this script relies on **Google Search** to locate course pages. However, **Google has anti-scraping measures**, so excessive searches can result in a temporary block. If this happens:
- Try running the script later.
- Use a VPN to change your IP.
- Reduce the number of searches per run.

## **How to Use It**
### **1. Gather Course IDs**
You first need a list of course IDs enclosed in `[]`. Here’s how to get them:
1. Go to the TUM **course catalog page** where all courses are listed.
2. Copy all course names and descriptions.
3. Paste them into ChatGPT with the prompt:
   > Extract all course IDs enclosed in `[]` from this text.
4. Save the result as a Python list called `id_list`.

### **2. Modify the Script**
- Replace `id_list` in the script with your extracted course IDs.
- Run the script and let it process each course automatically.

## **System Requirements**
This script requires:
- Python 3.x
- The following libraries:
  ```sh
  pip install beautifulsoup4 requests google
  ```

## **Limitations**
- If Google blocks too many searches, some courses will return **"No result found."**
- Some courses require **manual checking** if their structure differs from the standard TUM course pages.
- This tool is designed for both **Bachelor and Master students** at TUM.

## **License**
This project is licensed under the **MIT License**, meaning you can freely use, modify, and distribute it.

---

### **Contributing**
If you encounter issues or find ways to improve the script, feel free to open a pull request!

🚀 **Save time and optimize your electives effortlessly with this tool!**

