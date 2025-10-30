
# 🚀 Pytest + Playwright UI Automation Roadmap (4 Weeks)

A structured 4-week roadmap to master **UI automation with Pytest + Playwright** — from selectors and waits to full-framework, CI-ready test suites.  
Includes curated demo sites, weekly projects, and advanced extensions.

---

## 🗂️ Roadmap Overview

| Week | Focus | Core Outcome |
|------|--------|---------------|
| 1️⃣ | Foundations | Element locators, assertions, fixtures |
| 2️⃣ | Dynamic UI | Waits, network mocking, visual testing |
| 3️⃣ | Real-World Scenarios | Auth, files, shadow DOM, data-driven |
| 4️⃣ | Framework & CI | Page Objects, reports, GitHub Actions |
| 🧩 | Advanced | API + UI, visual diffs, Dockerization |

---

## 🧭 Week 1 – Foundations: Selectors & Assertions
<details>
<summary>📖 Expand</summary>

**🎯 Goal:** Master Playwright fundamentals within Pytest.

**Sites:**
- [Playwright Demo (Todo App)](https://demo.playwright.dev/todomvc/)
- [Rahul Shetty Automation Practice](https://rahulshettyacademy.com/AutomationPractice/)

**Skills:**
- Browser/page fixtures (`browser`, `page`)
- Locators: `get_by_role`, `locator`, `nth()`, CSS, XPath  
- Actions: click, type, checkbox, radio, keyboard (`page.keyboard.press("Enter")`)  
- Waits & assertions → `expect(locator).to_have_text()`, `page.wait_for_selector()`
- Dropdowns & alerts
- Basic screenshots & traces

**Mini Projects:**
- ✅ Add & verify items in Todo App  
- ✅ Automate form fill + assert success  
- ✅ Handle alert & assert text  
- ✅ Capture screenshot on success
</details>

---

## ⚡ Week 2 – Dynamic & Visual UI
<details>
<summary>📖 Expand</summary>

**🎯 Goal:** Handle async & tricky UIs confidently.

**Sites:**
- [UI Testing Playground](https://uitestingplayground.com/)
- [Demo QA](https://demoqa.com/)

**Skills:**
- Waits & timeouts for dynamic elements
- Hidden / disabled controls
- Hover, drag & drop, scroll into view
- Modals, tooltips, nested frames, iframes
- Network interception (`page.route`)
- Visual regression (`expect(page).to_have_screenshot()`)

**Mini Projects:**
- ✅ Test delayed button text  
- ✅ Drag & drop automation  
- ✅ iFrame form → assert result  
- ✅ Mock API response & verify  
- ✅ Visual toggle comparison
</details>

---

## 🌍 Week 3 – Realistic Scenarios & Flows
<details>
<summary>📖 Expand</summary>

**🎯 Goal:** Build end-to-end flows with data & auth.

**Sites:**
- [Herokuapp](https://the-internet.herokuapp.com/)
- [Swag Labs](https://www.saucedemo.com/)
- [Parabank](https://parabank.parasoft.com/)

**Skills:**
- Authentication (`page.authenticate`)
- Cookies & session storage
- File upload / download
- Infinite scroll & dynamic content
- Shadow DOM
- Multi-tab navigation
- Context auth (`storage_state.json`)
- Pytest hooks for screenshots on failure
- Parallel runs (`pytest -n auto`)
- Parameterization for data-driven tests

**Mini Projects:**
- ✅ Login (positive & negative)  
- ✅ File upload/download → verify  
- ✅ Infinite scroll until content loads  
- ✅ Swag Labs checkout flow  
- ✅ Parabank fund transfer assert balance
</details>

---

## 🧱 Week 4 – Framework & CI/CD
<details>
<summary>📖 Expand</summary>

**🎯 Goal:** Assemble a scalable, CI-ready framework.

**Sites:**  
UI Testing Playground | Swag Labs | Parabank | OpenCart | Tricentis Demo Shop

**Skills:**
- Page Object Model (POM): `tests/`, `pages/`, `utils/`, `fixtures/`
- Config files & `pytest.ini`
- Environment switching (`--env=staging`)
- Headed vs headless modes
- Reporting → `pytest-html`, `Allure`
- Playwright trace viewer
- CI/CD → GitHub Actions with browser matrix
- Dockerizing tests for CI isolation

**Final Project Checklist:**
- ✅ Unified framework covering 3+ sites  
- ✅ POM + fixtures + config  
- ✅ Screenshots & traces on failure  
- ✅ Allure/HTML reports  
- ✅ Parallel execution  
- ✅ GitHub Actions workflow  
- ✅ Repo pushed & documented
</details>

---

## 🧩 Stage 6 – Advanced Extensions (Optional)
<details>
<summary>📖 Expand</summary>

| Topic | Description |
|--------|-------------|
| **API + UI Hybrid Testing** | Combine REST API checks (`requests`) with UI validations. |
| **Component Testing** | Test React/Angular components with Playwright component mode. |
| **Visual Regression** | Image snapshot diff testing for UI changes. |
| **Custom Plugins** | Create Pytest hooks for logging & custom reporting. |
| **Docker Integration** | Containerize the entire framework for CI consistency. |
| **Cloud Grid Testing** | Run cross-browser tests on BrowserStack / LambdaTest. |
</details>

---

## 🧰 Tech Stack

- **Language:** Python 3.10+
- **Frameworks:** Playwright, Pytest
- **Reports:** Allure, pytest-html
- **CI/CD:** GitHub Actions / GitLab CI
- **Extras:** Docker, pytest-xdist, requests

---

## 🧾 Setup Instructions

```bash
# Clone
git clone https://github.com/<your-username>/pytest-playwright-roadmap.git
cd pytest-playwright-roadmap

# Install
pip install -r requirements.txt

# Run
pytest -v --headed --alluredir=reports

# View Allure Report
allure serve reports
