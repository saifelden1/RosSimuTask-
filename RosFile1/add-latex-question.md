# Add LaTeX Question Skill

## Purpose
Streamline adding questions and answers to the ROAR documentation (part1.tex) with automatic editing, compilation, and preview refresh.

## Workflow

When the user provides a question and answer:

1. **Extract Information**
   - Question number and title
   - Answer content
   - Identify which section it belongs to

2. **Edit and Improve**
   - Condense verbose explanations
   - Structure with clear formatting (bold headers, enumerations, bullet points)
   - Use LaTeX math symbols where appropriate (→, $\rightarrow$)
   - Keep technical accuracy while improving readability
   - Remove redundant phrases

3. **Add to Document**
   - Insert as new `\subsection{Q#: [Title]}`
   - Format answer with proper LaTeX structure
   - Maintain consistent style with existing questions

4. **Compile and Refresh**
   - Run `pdflatex part1.tex` twice (for TOC update)
   - Confirm successful compilation
   - Preview automatically refreshes

## Example Input Format

User provides:
```
Q3: [Question title]
[Answer content...]
```

## LaTeX Formatting Guidelines

- Use `\textbf{}` for emphasis
- Use `\begin{enumerate}` for numbered lists
- Use `\begin{itemize}` for bullet points
- Use `$\rightarrow$` for arrows in flow diagrams
- Use `\textit{}` for technical terms when nested in lists
- Keep paragraphs concise (2-3 sentences max)

## Error Handling

- If compilation fails, report the error and suggest fixes
- If question number is unclear, ask for clarification
- If answer is too long, suggest condensing before adding
