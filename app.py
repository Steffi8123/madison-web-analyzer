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
}

/* Background */
.main {
  background-color: var(--soft-bg);
}

/* Typography */
body {
  font-family: "Georgia", "Times New Roman", serif;
}

/* Button styling */
.stButton>button {
  background-color: var(--accent-blue);
  color: white;
  border-radius: 999px;
  padding: 0.5rem 1.6rem;
  border: none;
  font-weight: 600;
}
.stButton>button:hover {
  background-color: #1E48A8;
}

/* Metric card styling */
div[data-testid="metric-container"] {
  background: white;
  padding: 1rem;
  border-radius: 14px;
  border-left: 6px solid var(--primary-yellow);
  box-shadow: 0px 4px 14px rgba(0,0,0,0.04);
}

/* Dashboard headers */
h2, h3 {
  color: #1f2937;
  border-bottom: 2px solid var(--primary-amber);
  padding-bottom: 6px;
}

/* Info box */
.stAlert {
  background: #fff7ed;
  border-left: 6px solid var(--primary-amber);
}

/* Focus section highlight */
.section-highlight {
  background: white;
  border: 1px solid #e5e7eb;
  border-left: 6px solid var(--primary-yellow);
  padding: 1.2rem;
  border-radius: 16px;
  margin-bottom: 1rem;
}

/* Dataframe polish */
div[data-testid="stDataFrame"] {
  background: white;
  border-radius: 12px;
  border: 1px solid #e5e7eb;
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
st.markdown("## 📊 Analysis Dashboard", unsafe_allow_html=True)

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
