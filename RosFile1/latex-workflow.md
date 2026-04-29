# LaTeX Question Workflow

## Auto-Applied Behavior

When the user provides question content (with or without explicit "add Q#" instruction):

1. **Detect Question Content**
   - Look for question titles and answer text
   - Identify the next question number in sequence
   - Determine which section it belongs to (Section 1: Autonomous Systems, Section 2: ROS 2, etc.)

2. **Edit and Improve**
   - Condense verbose explanations
   - Structure with clear formatting (bold headers, enumerations, bullet points)
   - Use LaTeX math symbols where appropriate (→, $\rightarrow$)
   - Keep technical accuracy while improving readability
   - Remove redundant phrases

3. **Add to Document (ROARTASK/RosFile/part1.tex)**
   - Insert as new `\subsection{Q#: [Title]}`
   - Format answer with proper LaTeX structure
   - Maintain consistent style with existing questions

4. **Always Compile**
   - Run `pdflatex part1.tex` twice (for TOC update)
   - Confirm successful compilation
   - This refreshes the preview automatically

## LaTeX Formatting Guidelines

### Text Formatting
- Use `\noindent\textbf{}` for section subtitles (Core Components:, Key Policies:, etc.) to align them to the left
- Use `\textbf{}` for emphasis within text
- Use `\textit{}` for technical terms when nested in lists
- Keep paragraphs concise (2-3 sentences max)

### Lists
- Use `\begin{enumerate}[leftmargin=*]` for numbered lists
- Use `\begin{itemize}[leftmargin=*]` for bullet points

### Diagrams
- Convert workflow descriptions to TikZ diagrams instead of text
- Use simple box-and-arrow diagrams for system architectures
- Example TikZ structure:
```latex
\begin{center}
\begin{tikzpicture}[
    node distance=1.5cm,
    box/.style={rectangle, draw, thick, minimum width=2.8cm, minimum height=0.8cm, align=center, font=\small},
    arrow/.style={->, thick}
]
    % nodes and arrows here
\end{tikzpicture}
\end{center}
```

### Math and Symbols
- Use `$\rightarrow$` for arrows in flow diagrams
- Use proper LaTeX escaping for underscores: `\_`

## Document Structure

- Cover page with: Title, "Technical Documentation", Part number, Author name, Date
- Table of contents (auto-generated)
- Section 1: Autonomous Systems Fundamentals (Q1-Q4 as 1.1-1.4)
- Section 2: ROS 2 Fundamentals (Q1-Q2 as 2.1-2.2)
- Additional sections as needed

## Critical Rules

1. ALWAYS compile after adding/editing questions
2. ALWAYS use `\noindent\textbf{}` for subtitles to align left
3. ALWAYS convert workflow descriptions to diagrams
4. NEVER skip the compilation step
5. All content goes in part1.tex (no separate files)
