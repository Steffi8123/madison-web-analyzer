import streamlit as st
import pandas as pd

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Web Clarity & Empathy Analyzer",
    page_icon="✏️",
    layout="wide",
)

# ---------- SIMPLE BRANDING ----------
st.markdown("""
<style>
:root {
  --primary-yellow: #F9D342;
  --primary-amber: #F59E0B;
  --accent-blue:  #2563EB;
  --soft-bg: #F8FAFC;
  --text-dark: #1f2937;
  
}

/* Background */
.main {
  background: var(--soft-bg);
}

/* Typography */
body {
  font-family: "Georgia", "Times New Roman", serif;
  color: var(--text-dark);
}

/* Primary Button */
.stButton>button {
  background-color: var(--accent-blue);
  color: white;
  border-radius: 999px;
  padding: 0.55rem 1.7rem;
  border: none;
  font-weight: 600;
}
.stButton>button:hover {
  background-color: #1E48A8;
}

/* Dashboard metric cards - strong yellow contrast */
div[data-testid="metric-container"] {
  background: white;
  padding: 1.1rem;
  border-radius: 16px;
  border: 2px solid var(--primary-yellow);
  box-shadow: 0 6px 16px rgba(0,0,0,0.05);
}

/* Section containers */
.section-highlight {
  background: white;
  border: 2px solid var(--primary-yellow);
  border-left: 10px solid var(--primary-yellow);
  padding: 1.3rem;
  border-radius: 18px;
  margin-bottom: 1.5rem;
}

/* Headings (NO yellow text) */
h1, h2, h3 {
  color: var(--text-dark);
}

/* Divider style */
hr {
  border: none;
  height: 4px;
  background: var(--primary-yellow);
  border-radius: 999px;
  margin: 2rem 0;
}

/* Info box with amber contrast */
.stAlert {
  background: #fff8ed;
  border-left: 8px solid var(--primary-amber);
}

/* Dataframe contrast */
div[data-testid="stDataFrame"] {
  background: white;
  border-radius: 14px;
  border: 2px solid var(--primary-yellow);
}
/* Detail cards under Page deep-dive */
.detail-row {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  margin: 0.75rem 0 1.25rem 0;
}

.detail-card {
  background: white;
  border-radius: 16px;
  border: 1px solid #e5e7eb;
  padding: 0.9rem 1rem;
  box-shadow: 0 4px 12px rgba(0,0,0,0.04);
  flex: 1;
  min-width: 210px;
}

.detail-card-ux {
  border-left: 8px solid var(--primary-yellow);
}

.detail-label {
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #6b7280;
  margin-bottom: 0.1rem;
}

.detail-value {
  font-size: 1.2rem;
  font-weight: 600;
  color: #111827;
}

.detail-subtext {
  font-size: 0.9rem;
  color: #4b5563;
  margin-top: 0.35rem;
}
</style>


""", unsafe_allow_html=True)

# ---------- TITLE & INTRO ----------
st.title("✏️ Web Clarity & Empathy Analyzer")

st.write(
    "This is the first UI version of my Madison-based tool. "
    "Paste one or more URLs and the app will generate a demo report focusing on "
    "clarity, empathy, accessibility, and a few healthcare-inspired UX checks."
)

left, right = st.columns([2, 1])

with left:
    urls_text = st.text_area(
        "Paste URLs (one per line)",
        placeholder="https://example.com/page-1\nhttps://example.com/page-2",
        height=140,
    )
    run_button = st.button("Run analysis")

with right:
    st.markdown("#### What this tool focuses on")
    st.markdown(
        "- 🧠 **Clarity** – is the content easy to understand?\n"
        "- 💬 **Empathy** – does the tone feel supportive, not harsh?\n"
        "- ♿ **Accessibility** – basic WCAG-inspired checks (demo).\n"
        "- 🩺 **Healthcare-inspired UX** (non-clinical):\n"
        "  - Low-literacy friendliness\n"
        "  - Emotionally safe tone (no scary language)\n"
        "  - Clear information hierarchy\n"
        "  - Visual stress (dense blocks of text)\n"
    )
    st.info(
        "In a real deployment, this UI would call my Madison/n8n workflow and "
        "append results to a Google Sheet. For this assignment version, the "
        "analysis is mocked so you can see the interface and UX."
    )

# ---------- DUMMY ANALYSIS (REPLACE WITH REAL API LATER) ----------
def analyze_url_dummy(url: str) -> dict:
    """Demo analysis so the UI works even without a backend."""
    return {
        "url": url,
        # Core analysis
        "empathy_score": "Medium",
        "clarity_score": "High",
        "wcag_status": "Pass (AA demo)",
        "visual_schema": "Content-heavy layout",
        "summary": (
            "Demo summary: content is generally clear but could be simplified "
            "for low-literacy readers."
        ),
        "rewrite_suggestion": (
            "Shorten long sentences, reduce jargon, and add headings and "
            "bullet points for key actions."
        ),
        # Healthcare-inspired UX checks (non-clinical)
        "low_literacy_note": (
            "Contains a few long sentences; consider simpler language and "
            "shorter paragraphs."
        ),
        "tone_safety_note": (
            "Tone is mostly calm and neutral. Avoid phrases that sound "
            "alarming or judgmental."
        ),
        "hierarchy_note": (
            "Main message appears, but headings and bullets could be used "
            "more consistently."
        ),
        "visual_stress_note": (
            "Text blocks are a bit dense. Adding spacing and subheadings "
            "would reduce visual fatigue."
        ),
        "recommendations": [
            "Break long paragraphs into 2–3 shorter ones.",
            "Use headings for key sections like ‘What this means’ and ‘What to do next’.",
            "Replace medical jargon with patient-friendly words where possible.",
        ],
    }

# ---------- MAIN ACTION ----------
results = []

if run_button:
    # Collect URLs from textarea
    urls = []
    if urls_text.strip():
        urls = [u.strip() for u in urls_text.splitlines() if u.strip()]

    if not urls:
        st.warning("Please paste at least one URL.")
    else:
        st.info(f"Running demo analysis for {len(urls)} URL(s)…")

        for url in urls:
            data = analyze_url_dummy(url)
            results.append(data)

        # -------- Summary table --------
        df_rows = []
        for item in results:
            df_rows.append({
                "URL": item.get("url", ""),
                "Empathy": item.get("empathy_score", ""),
                "Clarity": item.get("clarity_score", ""),
                "WCAG": item.get("wcag_status", ""),
                "Visual schema": item.get("visual_schema", ""),
            })
        df = pd.DataFrame(df_rows)

        st.markdown("### Summary of results")
        st.dataframe(df, use_container_width=True)

        # ---------- DASHBOARD VIEW ----------
        st.markdown("## 📊 Analysis Dashboard")
        total_urls = len(df)
        high_clarity = (df["Clarity"] == "High").sum()
        good_empathy = df["Empathy"].isin(["Medium", "High"]).sum()
        wcag_pass = df["WCAG"].str.contains("Pass").sum()

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("URLs analyzed", total_urls)
        c2.metric("High clarity", f"{high_clarity}/{total_urls}")
        c3.metric("Supportive tone", f"{good_empathy}/{total_urls}")
        c4.metric("WCAG Pass", f"{wcag_pass}/{total_urls}")

        st.markdown("---")
        st.markdown("### 🧠 Clarity & Empathy comparison")

        score_map = {"Low": 1, "Medium": 2, "High": 3}
        chart_df = df.copy()
        chart_df["Clarity score"] = chart_df["Clarity"].map(score_map)
        chart_df["Empathy score"] = chart_df["Empathy"].map(score_map)
        chart_df = chart_df.set_index("URL")[["Clarity score", "Empathy score"]]

        st.bar_chart(chart_df)

        st.markdown("---")
        st.markdown("### 🔍 Page deep-dive")

        selected_url = st.selectbox(
            "Select a URL to view detailed insights:",
            df["URL"].tolist()
        )

        selected_item = next(item for item in results if item["url"] == selected_url)

        with st.container():
            st.markdown(f"#### {selected_url}")

            colA, colB = st.columns(2)

            with colA:
                st.write("**Empathy score:**", selected_item["empathy_score"])
                st.write("**Clarity score:**", selected_item["clarity_score"])
                st.write("**WCAG status:**", selected_item["wcag_status"])
                st.write("**Visual schema:**", selected_item["visual_schema"])

            with colB:
                st.write("**Summary**")
                st.write(selected_item["summary"])

                st.write("**AI rewrite suggestion**")
                st.write(selected_item["rewrite_suggestion"])

            st.markdown("#### 🩺 Healthcare-inspired UX checks")
            st.write("**Low-literacy friendliness:**", selected_item["low_literacy_note"])
            st.write("**Tone safety:**", selected_item["tone_safety_note"])
            st.write("**Information hierarchy:**", selected_item["hierarchy_note"])
            st.write("**Visual stress:**", selected_item["visual_stress_note"])

            st.markdown("**Recommendations**")
            for r in selected_item.get("recommendations", []):
                st.markdown(f"- {r}")

st.markdown("---")
st.markdown(
    "Back to my portfolio: [steffimanhalli.com](https://steffimanhalli.com)"
)
