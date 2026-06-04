# Guion de Presentación
## Inteligencia Artificial en Diagnóstico Médico
**Universidad Nacional · Sede Regional Brunca**
**Curso: Inteligencia Artificial · Prof. Pablo Andrés Venegas Elizondo**
**Expositor: Angel Stward Segura Méndez**

---

> **Cómo usar este guion**
> Cada sección indica: *(escena Manim)*, la **transición** para llegar a ella y el texto a decir.
> Las transiciones en `>` son las palabras exactas para cambiar de tema sin que suene abrupto.

---

## ESCENA 1 — Portada `S01_Portada`

*(el título aparece con fade in, logo UNA se ancla arriba)*

Buenos días. Me llamo Angel Segura y esta investigación se titula **"Inteligencia Artificial en Diagnóstico Médico"**.

En los próximos minutos vamos a recorrer juntos cómo una idea inspirada en el ojo humano está reescribiendo la forma en que los médicos detectan enfermedades.

---

## ✦ TRANSICIÓN 1→2 — De la portada a la realidad clínica

> *"Pero antes de hablar de algoritmos — déjenme mostrarles por qué esto importa ahora mismo, no en diez años."*

*(transición de fade out portada, fade in escena de resonancia magnética)*

---

## ESCENA 2 — Introducción `S02_Introduccion`

### Sub-escena A — El problema: diagnóstico humano bajo presión

En 2025, la FDA tiene **873 algoritmos de IA autorizados** solo en radiología.
Ese número no es accidental — viene de una necesidad real:

- Un radiólogo promedio revisa entre 50 y 100 estudios por día.
- Un nódulo pulmonar de 3 milímetros puede ser indistinguible del ruido en una tomografía cansada.
- El error diagnóstico en radiología oscila entre el 3 y el 5 % — en millones de estudios, eso son miles de casos perdidos.

### Sub-escena B — El punto de inflexión: AlexNet 2012

Todo cambió en **2012**. Una red convolucional llamada **AlexNet** entró a la competición ImageNet y dejó a los mejores algoritmos del mundo a más de 10 puntos porcentuales de diferencia.

El mensaje fue claro: las CNN podían **ver** — y hacerlo mejor que cualquier método anterior.

---

## ✦ TRANSICIÓN 2→3b — Del impacto al mecanismo

> *"Ahora la pregunta natural es: ¿cómo funciona todo esto por dentro? Para entender la CNN, primero necesitamos entender de dónde viene — la neurona artificial."*

---

## ESCENA 3b — Redes Neuronales Artificiales `S03b_ANN`

*(fórmula de la neurona aparece a la izquierda, gráfica de descenso del gradiente a la derecha)*

Una **neurona artificial** hace exactamente una cosa:

```
y = f( Σ wᵢ · xᵢ + b )
```

Toma entradas, las pesa, las suma, y aplica una función de activación.

Lo brillante es el aprendizaje. La red hace una predicción, la compara con la realidad usando la **función de pérdida `L = (y - y_real)²`**, y el backpropagation ajusta los pesos para reducir ese error — iteración tras iteración, bajando por la curva del gradiente hasta encontrar el mínimo.

El problema con estas redes para imágenes: si una imagen de 256×256 pixeles entra directo como vector, son **65,536 entradas**. La red pierde toda la estructura espacial. No sabe que dos pixeles vecinos forman un borde.

---

## ✦ TRANSICIÓN 3b→3c — De la ANN al ojo

> *"La solución no vino de la matemática — vino de la biología. De cómo nosotros mismos vemos el mundo."*

---

## ESCENA 3c — Introducción CNN `S03c_IntroCNN`

*(ojo gigante aparece a la derecha, lista de capas emerge a la izquierda)*

La corteza visual humana no procesa la escena completa de golpe. Empieza por detectar **bordes**, luego **esquinas**, luego **formas**, luego **objetos** completos.

Las CNN replican exactamente esa jerarquía. Las 6 capas que vamos a ver son:

| # | Capa | ¿Qué hace? |
|---|------|------------|
| 1 | **Input Layer** | Recibe la imagen — pixeles como neuronas |
| 2 | **Convolution** | Filtros deslizantes que detectan patrones |
| 3 | **ReLU** | Elimina señales negativas, introduce no-linealidad |
| 4 | **Pooling** | Reduce tamaño conservando lo importante |
| 5 | **Fully Connected** | Combina todo para razonar |
| 6 | **Softmax** | Convierte en probabilidades de diagnóstico |

---

## ✦ TRANSICIÓN 3c→4 — Del diagrama a la animación real

> *"Palabras aparte — veámoslo en vivo. Vamos a tomar el dígito ocho y pasarlo por cada capa, paso a paso."*

---

## ESCENA 4 — Capas de una CNN `S04_CapasCNN`

*(animación completa, paso a paso — 6 steps con demos interactivos)*

### Step 1 — Input Layer
La imagen entra como una grilla de pixeles. Cada valor entre 0 y 1 representa la intensidad. La estructura 2D se **preserva** — esa es la diferencia fundamental con las ANN.

### Step 2 — Convolution Layer
El filtro de 3×3 se desliza sobre la imagen multiplicando valores y sumando.

> *"Fíjense: azul es positivo — el filtro encontró un borde. Rojo es negativo — el gradiente va en dirección opuesta. El mapa muestra exactamente qué detectó el kernel en cada posición."*

Los tres kernels que vemos detectan: bordes horizontales, bordes verticales y el Laplaciano omnidireccional — el mismo tipo de detección que hace su retina ahora mismo.

### Step 3 — ReLU
```
ReLU(x) = max(0, x)
```
Simple pero poderoso. Todo lo negativo se va a cero. La red solo se queda con la señal positiva — las activaciones que realmente importan. El mapa se limpia.

### Step 4 — Max Pooling 2×2
De cada parche de 4 pixeles, solo sobrevive el máximo. El mapa se reduce a la mitad.

> *"¿Por qué quedarnos con el máximo? Porque si un borde apareció en algún lugar del parche — su valor máximo lo captura. Gana robustez frente a pequeñas variaciones de posición."*

### Step 5 — Fully Connected (Dense)
Los 75 valores del flatten se conectan a cada neurona de la capa densa. Aquí ya no hay estructura espacial — estamos razonando sobre combinaciones de características.

### Step 6 — Softmax & Output
```
softmax(zᵢ) = e^zᵢ / Σ e^zⱼ
```
El resultado: **98% de probabilidad de que sea el dígito 8**. Eso mismo aplica a "tumor vs. tejido sano" en una resonancia.

---

## ✦ TRANSICIÓN 4→5 — Del mecanismo a la escala

> *"Ahora que entendemos cómo ve una CNN — la pregunta es: ¿cómo aprende a ver millones de cosas sin ver millones de imágenes médicas etiquetadas? La respuesta es ImageNet."*

---

## ESCENA 5 — ImageNet y CADe/CADx `S05_ImageNet_CAD`

*(cuadrícula de imágenes ImageNet, luego división CADe vs CADx)*

**ImageNet**: 1.2 millones de imágenes, 1000 categorías. Una CNN entrenada aquí ya sabe detectar bordes, texturas, formas — habilidades que se transfieren directamente a la medicina.

**Transfer Learning**: tomamos esa red pre-entrenada y la re-entrenamos solo en la última capa con datos médicos específicos. El modelo ya inteligente aprende la tarea médica con una fracción de los datos y el tiempo.

**CADe vs CADx** — la distinción clínica clave:
- **CADe** *(Detection)*: *"¿Hay algo aquí?"* — localiza anomalías, reduce falsos negativos.
- **CADx** *(Diagnosis)*: *"¿Qué es esto y qué tan grave?"* — caracteriza, estadifica, recomienda.

---

## ✦ TRANSICIÓN 5→5b — Del concepto a la técnica de adaptación

> *"El transfer learning es el puente. Pero ¿cómo se construye ese puente cuando los datos médicos son escasos y están fragmentados entre hospitales?"*

---

## ESCENA 5b — Transfer Learning `S05b_TransferLearning`

*(arquitectura ResNet/U-Net con capas congeladas y descongeladas)*

La estrategia estándar:

1. **Congelar** las capas iniciales — ya saben detectar características generales.
2. **Fine-tune** solo las últimas capas — aprenden las particularidades médicas.
3. **Data augmentation** — rotaciones, flips, variaciones de brillo generan datos artificiales.

Resultado: U-Net segmenta tumores con un **coeficiente Dice** mayor al 85% entrenada con apenas cientos de imágenes, no millones.

---

## ✦ TRANSICIÓN 5b→6 — De la técnica a las arquitecturas que la aplican

> *"Cada tarea médica tiene su arquitectura ideal. Veamos las tres que dominan la literatura clínica actual."*

---

## ESCENA 6 — Arquitecturas Clave `S06_Arquitecturas`

*(comparación visual de AlexNet, U-Net, ResNet)*

| Arquitectura | Fortaleza | Uso médico principal |
|---|---|---|
| **AlexNet** | Pionera, validó el poder de las CNN profundas | Clasificación de imágenes (¿hay patología?) |
| **U-Net** | Encoder-decoder simétrico + skip connections | Segmentación píxel a píxel (delimitar tumor) |
| **ResNet** | Conexiones residuales — profundidad sin degradación | Alta precisión en patrones complejos (melanoma, tórax) |

> *"U-Net es elegante por su simetría: la rama izquierda extrae características, la rama derecha las reconstruye con precisión espacial. Las skip connections recuperan detalle fino que se perdería en la compresión."*

---

## ✦ TRANSICIÓN 6→7 — De los modelos a cómo los evaluamos

> *"Una arquitectura poderosa no sirve de nada si no sabemos medir honestamente qué tan bien funciona. Y en medicina, la medición incorrecta puede costar vidas."*

---

## ESCENA 7 — Métricas `S07_Metricas`

*(grid de 100 pacientes: 99 sanos, 1 enfermo — el scanner lo pinta todo de verde)*

### El espejismo de la precisión

Un modelo que marca a todos como sanos en una enfermedad de 1% de prevalencia tiene **99% de precisión** — y es completamente inútil clínicamente.

Por eso usamos:

**Sensibilidad** *(Recall)* — ¿Detectamos a todos los enfermos?
```
Sensibilidad = VP / (VP + FN)
```
Alta sensibilidad = pocos falsos negativos = pocas enfermedades perdidas.

**Especificidad** — ¿No alarmar innecesariamente a los sanos?
```
Especificidad = VN / (VN + FP)
```
Alta especificidad = pocos falsos positivos = pocos procedimientos innecesarios.

**AUC-ROC** — el resumen definitivo. Un AUC de 0.93 como el de los clasificadores de gliomas significa que el 93% de las veces el modelo separa correctamente a un enfermo de un sano.

> *"En diagnóstico crítico, preferimos alta sensibilidad aunque baje la especificidad — es mejor llamar a un paciente sano para una segunda prueba que perder un tumor."*

---

## ✦ TRANSICIÓN 7→8 — De las métricas a los sistemas reales que las cumplen

> *"Suficiente teoría. Veamos qué pasa cuando estos números se vuelven decisiones médicas en hospitales reales."*

---

## ESCENA 8 — Aplicaciones Reales `S08_Aplicaciones`

*(timeline de casos con logos y datos)*

### Viz.ai — Accidente Cerebrovascular
13 algoritmos FDA. 1,600+ hospitales. AUC > 0.90.
**Resultado:** reducción de **66 minutos** en inicio del tratamiento para oclusión de grandes vasos.
En ACV, cada minuto de demora destruye 1.9 millones de neuronas.

### Mirai — Cáncer de Mama (MIT)
C-index entre 0.69–0.78. Validado prospectivamente en **5 países**.
Personaliza los intervalos de cribado: pacientes de bajo riesgo esperan más, alto riesgo se monitorean más frecuentemente.

### Aidoc — Hemorragia Intracraneal
Sensibilidad > 90%. Funciona como triaje automático: el caso crítico sube al tope de la lista de trabajo del radiólogo.

### Shockmatrix — Trauma (Grenoble, Francia)
1,292 casos. La IA falló en 20 que los médicos detectaron. Los médicos fallaron en 21 que la IA identificó.
Ese resultado simétrico dice todo: **la combinación médico + IA supera a cualquiera de los dos solos**.

---

## ✦ TRANSICIÓN 8→9 — Del éxito a los límites honestos

> *"Sería irresponsable terminar con solo los éxitos. La tecnología tiene límites reales — y en medicina, ignorarlos tiene consecuencias."*

---

## ESCENA 9 — Limitaciones y Ética `S09_Limitaciones`

*(caja negra con luz interna + mapa de calor sobre radiografía)*

### 1. El problema del sesgo
Un modelo entrenado en pacientes predominantemente caucásicos puede fallar en otras poblaciones.
Un algoritmo validado con equipos Siemens puede perder 15 puntos de precisión con equipos GE.
La precisión del 95% en un hospital puede caer al 80% en otro con diferentes protocolos.

### 2. La caja negra
La CNN dice: *"94.7% de probabilidad maligna"*.
El radiólogo pregunta: *"¿Pero por qué?"*
La red no responde. Los métodos XAI *(mapas de saliencia, Grad-CAM)* muestran qué región activó la decisión — pero los clínicos frecuentemente los encuentran insuficientes para diagnósticos de vida o muerte.

### 3. Regulación que no avanza al mismo ritmo
La FDA y la MDR aprueban versiones **estáticas** de algoritmos. Cualquier actualización o reentrenamiento requiere un nuevo proceso de autorización completo.
Consecuencia: los modelos más seguros en papel pueden ser los más desactualizados en la práctica.

### 4. Responsabilidad legal en el limbo
El radiólogo que firma el informe es legalmente responsable — incluso si la IA contribuyó al error. Esta incertidumbre es la principal barrera de adopción que los estudios reportan.

> *"El 80% de los radiólogos europeos desconoce las regulaciones vigentes para IA médica. No por ignorancia, sino porque las regulaciones no están lo suficientemente claras todavía."*

---

## ✦ TRANSICIÓN 9→10 — De los problemas al horizonte

> *"Conocer los límites no es pesimismo — es la base para superarlos. Terminemos con lo que viene."*

---

## ESCENA 10 — Conclusiones `S10_Conclusiones`

*(diagrama de síntesis + perspectivas futuras)*

### Lo que queda demostrado

Las CNN han alcanzado **evidencia clínica sólida**:

| Tarea | Métrica | Valor |
|---|---|---|
| Clasificación de gliomas | AUC | 93.2% |
| Detección cáncer de mama | AUC | 89.6% |
| Hemorragia intracraneal | Sensibilidad | > 90% |
| Algoritmos FDA autorizados | Cantidad | 873 (mid-2025) |

### El horizonte — cuatro líneas de trabajo

1. **IA Explicable (XAI)** — que el modelo muestre *por qué* tomó la decisión, no solo *cuál fue*.
2. **Modelos Multimodales** — imagen + historial clínico + laboratorio + genómica en un solo modelo.
3. **IA Adaptativa** — marcos regulatorios que permitan reentrenamiento continuo con datos nuevos sin autorización completa cada vez.
4. **Aprendizaje Federado** — múltiples hospitales entrenan juntos sin compartir datos de pacientes.

### El mensaje final

> *"La IA no va a reemplazar al radiólogo. Va a convertir en obsoleto al radiólogo que no use IA."*

La colaboración entre **clínicos, ingenieros y reguladores** es la única ruta hacia una implementación equitativa, segura y efectiva.

Muchas gracias.

---

## Respuestas a preguntas frecuentes (backup)

**P: ¿Por qué solo el 2% de adopción plena si hay 873 algoritmos autorizados?**
R: Autorización ≠ integración. Los obstáculos son: costo de infraestructura de GPU, integración con sistemas PACS/HIS existentes, formación del personal, responsabilidad legal no resuelta y resistencia cultural al cambio.

**P: ¿Puede la IA equivocarse en un caso que el médico habría detectado?**
R: Sí, y el caso Shockmatrix lo confirma. Por eso el modelo ideal es colaborativo: la IA no reemplaza la decisión clínica, la informa y prioriza.

**P: ¿Cuándo será posible la IA adaptativa regulada?**
R: La FDA propuso el marco de "ciclo de vida total del producto" en 2021. A 2025 los protocolos detallados aún están en desarrollo. La estimativa de los expertos es regulación funcional entre 2026 y 2028.

**P: ¿Qué es el AI drift?**
R: La degradación progresiva del rendimiento de un modelo cuando la distribución de datos reales en producción empieza a diferir de los datos de entrenamiento. Un modelo que funcionó al 95% al lanzarse puede estar al 80% dos años después sin que nadie lo haya notado.
