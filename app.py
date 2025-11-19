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
}
body {
  font-family: "Georgia", "Times New Roman", serif;
}
.stButton>button {
  background-color: var(--accent-blue);
  color: white;
  border-radius: 999px;
  padding: 0.4rem 1.4rem;
  border: none;
}
.stButton>button:hover {
  background-color: #1E48A8;
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
    """Demo analysis so the UI works even without a backend.

    In the real version, this would call my Madison/n8n flow and return
    scores plus UX recommendations.
    """
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

# Later, when you have a real endpoint, you can swap to:
# def analyze_url_real(url: str) -> dict:
#     resp = requests.post("https://YOUR-ENDPOINT-HERE", json={"url": url}, timeout=60)
#     resp.raise_for_status()
#     return resp.json()


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

        # -------- Detailed view per URL --------
        st.markdown("### Detailed insights by URL")
        for item in results:
            url = item.get("url", "Unknown URL")
            with st.expander(url):
                st.markdown("#### Core content analysis")
                st.write("**Empathy score:**", item.get("empathy_score"))
                st.write("**Clarity score:**", item.get("clarity_score"))
                st.write("**WCAG status:**", item.get("wcag_status"))
                st.write("**Visual schema:**", item.get("visual_schema"))

                st.write("**Summary**")
                st.write(item.get("summary", ""))

                st.write("**AI rewrite suggestion**")
                st.write(item.get("rewrite_suggestion", ""))

                st.markdown("#### 🩺 Healthcare-inspired UX checks (non-clinical)")
                st.write("**Low-literacy friendliness:**", item.get("low_literacy_note"))
                st.write("**Tone safety:**", item.get("tone_safety_note"))
                st.write("**Information hierarchy:**", item.get("hierarchy_note"))
                st.write("**Visual stress:**", item.get("visual_stress_note"))

                st.write("**Recommendations**")
                for r in item.get("recommendations", []):
                    st.markdown(f"- {r}")

st.markdown("---")
st.markdown(
    "Back to my portfolio: [steffimanhalli.com](https://steffimanhalli.com)"
)
