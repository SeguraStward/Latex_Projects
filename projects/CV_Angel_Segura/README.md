# CVs — Angel Stward Segura Mendez

English-language CVs targeting four well-paid IT specializations a Systems Engineer
can grow into. All share one style/contact file and compile to a clean, single-page,
ATS-friendly PDF.

## Files

| File | Target role |
|---|---|
| `cv_ai_ml_engineer.tex` | AI / Machine Learning Engineer |
| `cv_cloud_devops.tex` | Cloud / DevOps / Platform Engineer |
| `cv_cybersecurity.tex` | Cybersecurity Engineer |
| `cv_backend_data.tex` | Backend / Data Engineer |
| `cv_python_reviewer_en.tex` | Junior Python Developer / Code Reviewer & Maintainer (English) |
| `cv_python_reviewer_es.tex` | Desarrollador Python Junior / Revisor y Mantenedor de Código (Español) |
| `cover_letter_python_reviewer_en.tex` | Cover letter for the Python reviewer role (English, fill in `[Company Name]`/`[Hiring Manager]`) |
| `cover_letter_python_reviewer_es.tex` | Carta de presentación para el rol de revisor Python (Español, completar `[Nombre de la Empresa]`/`[Nombre del Reclutador]`) |
| `cvstyle.tex` | Shared style + personal/contact data for English docs (edit once here) |
| `cvstyle_es.tex` | Same shared style, with Spanish `babel` for the Spanish-language docs |

## How to compile

These CVs are **separate `.tex` files**, so `./compile.sh` (which targets `main.tex`)
does not build them directly. Compile each one with `latexmk` inside the Docker image:

```bash
# From the repo root:
docker compose run --rm latex "cd projects/CV_Angel_Segura && latexmk -pdf cv_ai_ml_engineer.tex"
```

Or build all four at once:

```bash
docker compose run --rm latex "cd projects/CV_Angel_Segura && \
  for f in cv_*.tex; do latexmk -pdf \"\$f\"; done"
```

> Requires the full TeX Live image (it ships `lato`, `fontawesome5`, `enumitem`,
> `titlesec`). `cvstyle.tex` includes fallbacks, so it still compiles without those
> packages — just without the Lato font and icons.

## Editing your data

All contact info lives in **`cvstyle.tex`** (English docs) and **`cvstyle_es.tex`**
(Spanish docs) via `\My...` commands: name, phone, email, location, LinkedIn, GitHub,
LeetCode. Change it once in each file and every CV in that language updates.

## Strategy / how to use these

Each CV is honest about being **junior / entry-level oriented to grow**:

- **Professional Summary** — positions you for the target role.
- **Technical Skills** — what you can already touch, with a `Currently strengthening`
  line listing the high-value skills to study next.
- **Key Projects** — your real projects (Andromeda API, BotFlow, DocParser, spam
  detector, neural-network visualizations, SecurePipe, NestJS testing), framed for
  each role.
- **Learning Roadmap & Target Certifications** — the certs/skills to pursue. Treat
  this as your **study plan**: as you complete each item, move it up into Skills.

### Suggested study order per role
- **AI/ML:** Python + scikit-learn → DeepLearning.AI specializations → TensorFlow/PyTorch → MLOps → AWS ML.
- **Cloud/DevOps:** Linux + Docker → AWS Cloud Practitioner → Terraform Associate → CKA (Kubernetes) → observability.
- **Cybersecurity:** Networking + Linux → CompTIA Security+ → TryHackMe/HTB → eJPT → cloud security.
- **Backend/Data:** SQL + FastAPI/NestJS → databases & modeling → Spark/Airflow → data warehousing → AWS Data Engineer.

Keep your projects' GitHub links up to date — recruiters click them.
