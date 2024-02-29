import numpy as np
import math
import random as r

d = (1 + 0.04*np.random.rand(1000) - 0.5)
t = (1 + 0.02*np.random.rand(1000) - 0.5)
f = t/d

fmaks = np.max(np.abs(f - 1))/1
print(f"Maks feil: {np.round(42*fmaks,3)}%")

\documentclass[a4paper,10pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[norsk]{babel}
\usepackage{amsmath, amssymb, amsthm}

\title{Løsningsforslag}
\author{Ditt Navn}
\date{\today}

\begin{document}

\maketitle

\section*{Oppgave 3}

DJ Svensson sier seg imponert over problemløsningsøkten din. Styrket av fremgangen i oppgave 2, og DJ Svenssons tilbakemelding, prøver du på neste trinn: du ønsker egentlig å beregne en funksjon $\theta$:
\[
\theta = \cos^{-1} f = \cos^{-1} \frac{c\pi}{d}
\]

\begin{enumerate}
    \item[(a)] Utled et uttrykk for maksimal relativ feil for verdien av $\theta$, dvs
    \[
    \frac{|\Delta\theta|}{|\theta|}_{\text{maks}}
    \]
    
    \item[(b)] Er den
