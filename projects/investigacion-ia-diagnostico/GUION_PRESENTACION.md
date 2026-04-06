# Guion de Presentacion: IA en Diagnostico Medico

> **Duracion estimada:** 12-15 min | **Formato:** Presentacion con animaciones Manim
> **Tip:** Cada seccion inicia con una frase gancho. Las transiciones estan marcadas con `>>`. Los datos clave estan en **negritas**.

---

## S01 — Portada (~30s)

**[En pantalla: red neuronal armandose capa por capa, pulso de activacion, tarjetas con metricas AUC 0.932 / Sens 94.7% / Espec 91.2%, fade a titulo]**

> *No hablar todavia. Dejar que la animacion capture la atencion.*

Cuando aparezca el titulo, presentarse:

> "Buenos dias/tardes. Mi nombre es Angel Stward Segura Mendez. Esta investigacion explora como el Deep Learning, especificamente las redes neuronales convolucionales, esta transformando el diagnostico medico por imagen."

>> **Transicion:** "Para entender por que esto importa, empecemos con un dato..."

---

## S02 — Introduccion (~1 min)

**[En pantalla: MRI cerebral simulada a la izquierda, CNN al centro procesando, resultado "Tumor 94.7%"]**

> "Imaginen una resonancia magnetica. Un radiologo promedio la analiza en varios minutos. Una CNN entrenada puede detectar un tumor en segundos, con una confianza del 94.7%. Pero esto no es ciencia ficcion — es el presente."

Puntos clave a mencionar conforme aparecen los bullets:

1. **Deep Learning revoluciona el diagnostico** — "No es una mejora incremental, es un cambio de paradigma en como procesamos imagenes medicas."
2. **Radiologia, Dermatologia, Oftalmologia** — "Los tres campos donde mayor impacto ha tenido."
3. **AlexNet 2012** — "Todo cambio cuando AlexNet demostro que las CNNs podian superar cualquier metodo anterior en reconocimiento de imagenes."
4. **CNN supera a especialistas** — "En ciertas tareas especificas y controladas."
5. **FDA autoriza modelos como copilotos** — "No reemplazos, copilotos clinicos."
6. **Elimina handcrafted features** — "La red aprende sola que rasgos importan — ya no necesitamos programar manualmente que buscar."

>> **Transicion:** "Pero, como funciona una red neuronal? Vamos a abrir la caja negra."

---

## S03 — ANN vs CNN (~1.5 min)

**[En pantalla: izquierda ANN clasica (3 capas), derecha CNN inspirada en corteza visual]**

> "Empecemos por lo basico. Una red neuronal artificial tiene neuronas conectadas en capas: entrada, oculta y salida. Cada conexion tiene un peso que se ajusta durante el entrenamiento."

Senalar el diagrama de la ANN:

> "Funciona bien para datos tabulares, pero tiene un problema critico con imagenes..."

Cuando aparezca la caja roja con los problemas:

> "Si tomas una imagen 2D y la aplanas a un vector 1D, pierdes toda la estructura espacial. Es como intentar entender un cuadro de Picasso leyendo los valores RGB uno por uno."

Cuando aparezca el ojo y la flecha central:

> "Las CNNs resuelven esto. Estan inspiradas en la corteza visual humana — procesan la imagen preservando las relaciones espaciales entre pixeles."

>> **Transicion:** "Veamos exactamente como una CNN procesa una imagen, paso a paso."

---

## S04 — Capas de una CNN (~2 min)

**[En pantalla: grid de pixeles formando el digito "8", procesamiento capa por capa]**

> "Vamos a seguir el viaje de un simple digito 8 a traves de una CNN."

**Acto 1 — Entrada:**
> "Empezamos con una imagen de 7 por 6 pixeles. Cada pixel tiene un valor entre 0 y 1. Esto es todo lo que la red recibe: numeros."

**Acto 2 — Detectores de bordes:**
> "La primera capa convolucional tiene **128 filtros** que solo detectan rasgos primitivos: bordes horizontales, verticales y diagonales. Cada filtro es una matriz pequena que se desliza sobre la imagen buscando un patron especifico."

*Enfatizar:* "Importante: esta capa NO sabe que es un 8. Solo ve bordes y esquinas."

**Acto 3 — Detectores de formas:**
> "La segunda capa combina esos bordes en formas mas complejas. Aqui la red detecta que hay **dos bucles** — uno arriba y uno abajo. Esto es lo que distingue un 8 de un 0, un 6, o un 9."

**Acto 4 — Softmax:**
> "La capa final tiene 10 neuronas, una por digito. La funcion Softmax convierte las activaciones en probabilidades. El 8 gana con un **98%** de confianza."

*Concepto clave:* "Esto es lo que hace poderosas a las CNNs: **aprenden jerarquicamente** — de lo simple a lo complejo, de bordes a formas a conceptos."

>> **Transicion:** "Ahora, en medicina no clasificamos digitos sino patologias. Aqui es donde entran CADe y CADx."

---

## S05 — ImageNet, CADe y CADx (~1 min)

**[En pantalla: radiografia con bounding box (CADe) vs barras de probabilidad benigno/maligno (CADx)]**

> "Hay dos formas en que la IA asiste al medico."

Senalar el lado izquierdo:
> "**CADe** — Deteccion asistida. Responde: hay algo ahi? Dibuja una caja alrededor de una anomalia. Su objetivo es **reducir falsos negativos**, que no se escape nada."

Senalar el lado derecho:
> "**CADx** — Diagnostico asistido. Responde: que es eso? Dice: **85% maligno, 15% benigno**. Caracteriza la patologia."

Cuando aparezca la grilla de ImageNet:
> "Pero para que estas redes funcionen necesitan datos. ImageNet fue la base de datos que lo cambio todo: **1.2 millones de imagenes en 1000 categorias**. Y en 2012, AlexNet demostro que una CNN profunda podia ganar la competencia de reconocimiento de imagenes."

>> **Transicion:** "Pero hay un problema: en medicina no tenemos millones de imagenes. La solucion es Transfer Learning."

---

## S05b — Transfer Learning (~1 min)

**[En pantalla: dominio fuente (ImageNet, 1.2M imagenes) -> flecha -> dominio destino (imagenes medicas, ~500 muestras)]**

> "Aqui esta la magia. Una red entrenada con **1.2 millones** de fotos de perros, gatos y autos ya aprendio a detectar bordes, texturas y patologias visuales genericas."

> "Con Transfer Learning, tomamos esa red pre-entrenada y la **adaptamos** al dominio medico con apenas **500 muestras**. Las primeras capas ya saben ver — solo reentrenamos las ultimas para que aprendan a ver tumores en vez de gatos."

*Dato clave:* "Esto es lo que hizo viable la IA medica: no necesitas millones de radiografias etiquetadas, necesitas un buen punto de partida."

>> **Transicion:** "Con esto claro, veamos las tres arquitecturas que dominan el diagnostico medico."

---

## S06 — Arquitecturas: AlexNet, U-Net, ResNet (~2 min)

**[En pantalla: pipeline de AlexNet, arquitectura encoder-decoder de U-Net, bloque residual de ResNet]**

**AlexNet — Clasificacion:**
> "AlexNet fue la pionera. Arquitectura simple: capas convolucionales, pooling, y capas fully connected al final. Dice: tumor si o no. Alcanzo **90.2% de precision** en clasificacion pulmonar."

**U-Net — Segmentacion:**
> "Pero a veces no basta con saber SI hay tumor — necesitas saber DONDE exactamente. U-Net tiene una arquitectura de encoder-decoder con skip connections."

*Senalar las conexiones:* "El encoder comprime la imagen, el decoder la reconstruye pixel por pixel. Las skip connections preservan el detalle espacial. Es el **estandar actual** para segmentacion medica — segmentacion cardiaca, delineacion de tumores."

**ResNet — Precision profunda:**
> "El problema con redes muy profundas es que el gradiente desaparece. ResNet lo resuelve con conexiones residuales: **y = F(x) + x**. La red puede tener 50, 100, 150+ capas sin degradacion."

*Dato clave:* "ResNet alcanzo un **AUC de 93.2%** en clasificacion de gliomas cerebrales."

Cuando aparezca la tabla comparativa:
> "En resumen: AlexNet clasifica, U-Net segmenta, ResNet profundiza. Cada una resuelve un problema distinto."

>> **Transicion:** "Ahora bien, cuando decimos que un modelo tiene 93% de AUC... que significa realmente?"

---

## S07 — Metricas: ROC, Sensibilidad, Especificidad, AUC (~2 min)

**[En pantalla: grilla de 100 puntos, 99 verdes + 1 rojo]**

**Acto 1 — El espejismo de la precision:**
> "Miren esta grilla. 99 pacientes sanos, 1 enfermo. Si el modelo dice que TODOS estan sanos, tiene **99% de precision**. Suena increible, verdad?"

*Pausa dramatica cuando se revela el punto rojo:*
> "Pero acaba de perder al unico paciente con cancer. En medicina, ese **1% de error puede ser fatal**. Por eso la precision sola no sirve."

**Acto 2 — Las dos balanzas:**
> "Necesitamos dos metricas complementarias."

Senalar izquierda: "**Sensibilidad**: de todos los enfermos, cuantos detectamos? TP sobre TP mas FN. Queremos que sea alta para no dejar escapar enfermos."

Senalar derecha: "**Especificidad**: de todos los sanos, cuantos descartamos correctamente? TN sobre TN mas FP. Queremos que sea alta para no alarmar innecesariamente."

Cuando aparezca el slider:
> "Aqui esta el dilema: si bajo el umbral de deteccion, atrapo mas enfermos pero tambien genero mas falsas alarmas. Es un **trade-off** constante."

**Acto 3 — Curva ROC:**
> "La curva ROC grafica este trade-off. El eje X son las falsas alarmas, el eje Y la sensibilidad. La diagonal es adivinar al azar. Nuestra curva amarilla es un buen modelo: en este punto opera con **78% de sensibilidad** pagando solo **20% de falsas alarmas**."

**Acto 4 — AUC:**
> "El AUC resume todo en un solo numero. **0.50** es lanzar una moneda, **1.00** es perfecto. Nuestro modelo tiene **AUC 0.932** — excelente, pero no perfecto. Y esa diferencia del 7% en medicina puede significar vidas."

>> **Transicion:** "Con estas metricas claras, veamos que esta pasando en el mundo real."

---

## S08 — Aplicaciones Reales (~1.5 min)

**[En pantalla: 5 tarjetas con casos de implementacion, luego impacto clinico]**

> "Estas no son promesas de laboratorio. Son sistemas funcionando hoy en hospitales."

Conforme aparece cada tarjeta:

1. **Viz.ai** — "Detecta accidentes cerebrovasculares con un AUC superior a 0.90. Esta en mas de **1,600 hospitales** y ha reducido el tiempo de tratamiento en **66 minutos**. En un ACV, cada minuto cuenta."

2. **Mirai (MIT)** — "Predice riesgo de cancer de mama a **5 anos** con un C-index de 0.69 a 0.78. Validado en 5 paises. Esto permite un cribado personalizado, no el mismo protocolo para todas."

3. **Aidoc** — "Detecta hemorragia intracraneal con sensibilidad mayor al **90%**. Hace triaje automatico: prioriza los casos criticos en la cola del radiologo."

4. **Qure.ai** — "Detecta nodulos pulmonares, aprobado por la FDA. Segmentacion en tomografia para cribado de cancer de pulmon."

5. **Shockmatrix** — "Estudio con 1,292 casos de trauma que demostro algo crucial: **IA y medicos son complementarios**. Juntos detectan mas que por separado."

Cuando aparezcan los bullets de impacto:
> "El dato mas revelador: a mediados de 2025, la FDA habia autorizado **873 algoritmos de IA** en radiologia. Esto ya no es experimental."

>> **Transicion:** "Pero... si todo esto funciona tan bien, por que solo el 2% de los hospitales en EE.UU. lo usan? Porque hay barreras reales."

---

## S09 — Limitaciones y Desafios Eticos (~1.5 min)

**[En pantalla: Hospital A (95%) vs Hospital B (~80%), caja negra, tarjetas de desafios]**

**Sesgo y Generalizacion:**
> "Este es el problema numero uno. Un modelo entrenado en el Hospital A, con su equipo y su poblacion, alcanza **95% de precision**. Pero cuando lo llevas al Hospital B, con equipo diferente y otra demografia, cae a **80%**. Una caida del **15%** que puede significar diagnosticos erroneos."

**Caja Negra:**
> "Segundo problema: la interpretabilidad. El modelo dice 'maligno, 94.7%', pero no dice POR QUE. Existen tecnicas como Grad-CAM y SHAP que intentan explicar, pero los radiologos las encuentran insuficientes para confiar ciegamente."

Cuando aparezcan las 4 tarjetas:

> **Regulacion:** "La FDA aprueba versiones estaticas. Si el modelo aprende y se actualiza, necesita una nueva autorizacion. Esto frena la IA adaptativa."

> **Responsabilidad:** "Si la IA se equivoca, quien responde? Hoy, el radiologo firma y asume toda la responsabilidad legal."

> **Integracion:** "Muchos hospitales tienen sistemas PACS y RIS de hace decadas. Integrar IA ahi es un desafio tecnico enorme."

> **Escalabilidad:** "GPUs caras mas etiquetado por expertos igual a costos prohibitivos para clinicas pequenas."

Cuando aparezca la frase final:
> "La conclusion es clara: **la IA es un copiloto, no un reemplazo del especialista**."

>> **Transicion:** "Para cerrar, que nos dicen los datos y hacia donde vamos."

---

## S10 — Conclusiones y Perspectivas Futuras (~1.5 min)

**[En pantalla: hallazgos clave apareciendo uno por uno, luego perspectivas futuras, luego galeria]**

**Sintesis:**
> "Recapitulemos lo que encontramos."

1. "ResNet alcanzo un **AUC de 93.2%** en gliomas y **89.6%** en cancer de mama."
2. "Aidoc logra **sensibilidad mayor al 90%** en hemorragia intracraneal."
3. "U-Net se ha consolidado como el **estandar para segmentacion** medica."
4. "Hay **873 algoritmos autorizados** por la FDA, el 78% de todas las aprobaciones de IA medica son en radiologia."
5. "Pero la adopcion plena es de apenas el **2%** en Estados Unidos."

**Perspectivas futuras:**
> "Hacia donde va esto?"

1. "**IA Explicable (XAI)** — Eliminar la caja negra para que los medicos confien en las decisiones."
2. "**Modelos multimodales** — Combinar imagen con historial clinico y laboratorio. MedSAM ya esta explorando esto."
3. "**IA Adaptativa** con marcos regulatorios que permitan actualizaciones continuas."
4. "**Aprendizaje Federado** — Entrenar modelos entre hospitales sin compartir datos de pacientes. Privacidad y precision al mismo tiempo."

**Durante la galeria de imagenes:**
> *Dejar que las imagenes hablen. Si se desea, hacer un breve comentario sobre cada una:*
> "Resonancia, segmentacion tumoral, radiografia digital, visualizacion de capas, arquitectura U-Net... cada imagen representa un paso en esta revolucion."

**Cierre:**
> "Las CNNs han demostrado que pueden igualar e incluso superar a especialistas en tareas especificas. Pero el camino de la ecuacion al paciente todavia requiere resolver sesgo, regulacion y confianza. El futuro no es IA versus medicos — es IA CON medicos. Gracias."

---

## Tips para la Presentacion

- **Ritmo:** No correr. Las animaciones estan disenadas para dar tiempo visual. Hablar MIENTRAS se animan, no despues.
- **Contacto visual:** Mirar a la audiencia, no a la pantalla. Conocer la secuencia de memoria.
- **Datos ancla:** Los 3 numeros que deben recordar: **AUC 0.932**, **873 algoritmos FDA**, **2% adopcion**. Repetirlos crea coherencia narrativa.
- **Tono:** Tecnico pero accesible. Evitar jerga sin explicar. Si dicen "Softmax", explicar que hace.
- **Preguntas comunes:**
  - *"Puede la IA reemplazar al radiologo?"* — No. Copiloto, no piloto. Solo 2% de adopcion lo demuestra.
  - *"Que tan confiable es?"* — AUC 0.93 es excelente, pero el sesgo por poblacion es real.
  - *"Como se protege la privacidad?"* — Aprendizaje federado: el modelo viaja, los datos no.
