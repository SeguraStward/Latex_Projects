# GUION DE PRESENTACIÓN
## Inteligencia Artificial en Diagnóstico Médico
### Universidad Nacional — Curso de Inteligencia Artificial
**Presentador:** Ángel Stward Segura Méndez  
**Formato:** Narración sincronizada con video animado (Manim)

---

> **Cómo leer este guion**
> Cada sección incluye:  
> `[PANTALLA]` → descripción de lo que ocurre en pantalla en ese momento  
> **Texto en negrita** → énfasis vocal  
> *(pausa)* → momento para respirar / dejar que la animación respire

---

---

## ESCENA 1 — PORTADA `S01_Portada`

---

### FASE 1 — Red neuronal aparece capa por capa *(~4 seg)*

`[PANTALLA: Fondo negro. Los nodos de la primera capa aparecen uno a uno — azul claro. Las conexiones se dibujan hacia la siguiente capa. El proceso se repite capa por capa hasta completar la red.]`

*(silencio o música de fondo — dejar que la imagen hable)*

---

### FASE 2 — Forward pass + métricas *(~5 seg)*

`[PANTALLA: Los nodos se iluminan en secuencia de izquierda a derecha — el "pulso" de información. Abajo aparecen tres tarjetas: AUC 0.932 · Sensibilidad 94.7% · Especificidad 91.2%]`

*(silencio — dejar que las métricas sean la primera impresión)*

---

### FASE 3 — Fade a negro *(~2 seg)*

`[PANTALLA: La red y las métricas desaparecen suavemente.]`

*(pausa corta)*

---

### FASE 4 — Pantalla de portada completa *(~8 seg)*

`[PANTALLA: Aparece el encabezado "Universidad Nacional · Sede Regional Brunca". El título principal: "Inteligencia Artificial en Diagnóstico Médico". Subtítulo: Deep Learning · CNN · Diagnóstico por Imagen. Nombre del docente y del estudiante. Fecha: Marzo 2026.]`

Buenos días. Mi nombre es Ángel Segura y hoy les voy a hablar de algo que, en este momento, está cambiando la manera en que los médicos diagnostican enfermedades.

*(pausa de 2 seg)*

¿Qué pasa cuando una computadora aprende a ver — y no solo a ver, sino a detectar lo que ningún ojo entrenado alcanza a percibir a tiempo?

---

---

## ESCENA 2 — INTRODUCCIÓN `S02_Introduccion`

---

### Sub-escena A — MRI cerebral + CNN detectando el tumor *(~12 seg)*

`[PANTALLA: Título "Introducción". A la izquierda aparece un cerebro simulado con resonancia magnética — se distingue una mancha roja: el tumor. Una línea de escaneo barre la imagen de arriba a abajo. La CNN en el centro comienza a procesar. Aparecen bounding boxes falsos — la red "tantea". Luego los nodos se iluminan capa por capa en el forward pass.]`

Durante años, los médicos analizaban imágenes — rayos X, resonancias, tomografías — de forma manual. Y cuando llegaron los sistemas asistidos por computadora, los primeros CAD, no fueron suficientes. Los radiólogos frecuentemente obtenían mejores resultados solos.

*(pausa)*

`[PANTALLA: Aparece el bounding box verde sobre el tumor: "Tumor 94.7%". Una flecha verde apunta a la derecha con la palabra "Diagnóstico".]`

Pero entonces llegó el **Deep Learning**. Y todo cambió.

---

### Sub-escena B — Puntos clave *(~15 seg)*

`[PANTALLA: La red y el escaneo desaparecen. A la derecha van apareciendo uno a uno, con un punto teal, los 6 puntos clave: Deep Learning revoluciona el diagnóstico · Radiología | Dermatología | Oftalmología · AlexNet (2012): punto de inflexión en ImageNet · CNN supera a especialistas en ciertas tareas · FDA autoriza modelos como copilotos clínicos · Elimina handcrafted features]`

Las redes neuronales convolucionales — las CNN — transformaron el diagnóstico por imagen. Se utilizan hoy en radiología, dermatología, oftalmología...

*(señalar mientras aparece cada punto)*

En **2012**, AlexNet ganó la competición de ImageNet con una diferencia tan aplastante que el mundo científico no pudo ignorarlo. Desde ese día, estas redes comenzaron a rendir **igual o mejor** que especialistas experimentados en tareas concretas.

La FDA, el organismo regulador más estricto del mundo para dispositivos médicos, ya ha **autorizado 873 algoritmos** de IA en radiología para mediados de 2025. No como sustitutos del médico — sino como **copilotos bajo supervisión**.

Y la clave técnica es elegante: estas redes **eliminan la necesidad** de definir manualmente qué buscar. La CNN aprende sola a extraer patrones complejos directamente de los píxeles.

---

---

## ESCENA 3 — ANN vs CNN `S03_ANN_CNN`

---

### Sub-escena A — Neurona artificial + red ANN *(~12 seg)*

`[PANTALLA: Título "Redes Neuronales: ANN vs CNN". A la izquierda aparece una neurona con entradas x1, x2, x3, pesos w1, w2, w3, la suma Σ en el centro y la salida y. Debajo, la red ANN completa con capas de entrada, oculta y salida. En rojo: "Imagen 2D a vector 1D — Pierde estructura espacial".]`

Para entender las CNN, primero entendamos de dónde vienen.

Una **red neuronal artificial** — o ANN — es un modelo computacional inspirado en el cerebro. Cada neurona recibe señales, las pondera con sus pesos, y produce una salida. Ensamblando miles de estas neuronas en capas, la red aprende.

El problema con las ANN para imágenes es este: para procesarlas, hay que **aplanar** la imagen en un vector de una sola dimensión. Un píxel deja de tener vecinos. La relación espacial — "este píxel está arriba de este otro" — se pierde completamente.

---

### Sub-escena B — División central y CNN con el ojo *(~10 seg)*

`[PANTALLA: Una línea punteada divide la pantalla. Flecha en el centro: "Inspirada en la corteza visual". A la derecha aparece el título "Red Neuronal Convolucional (CNN)" y debajo, el ojo animado — el iris se mueve de derecha a izquierda y vuelve al centro. Texto: "Corteza Visual Humana".]`

La solución vino de la biología. Las CNN están **inspiradas en cómo funciona la corteza visual humana**: detectamos primero bordes, luego formas, luego objetos completos — en jerarquía.

*(señalar el ojo)*

Este ojo representa exactamente eso: una arquitectura diseñada para procesar espacio visual de manera eficiente. En lugar de destruir la estructura 2D de la imagen, las CNN la preservan y explotan.

---

---

## ESCENA 4 — CAPAS DE UNA CNN `S04_CapasCNN`

---

### Acto 1 — Capa de Entrada *(~10 seg)*

`[PANTALLA: "Capa de Entrada". El número 8 vectorial aparece. Sobre él desciende una cuadrícula de píxeles 7x6. Texto: "7x6 píxeles — valor entre 0 y 1 por pixel". La cuadrícula se comprime a la izquierda. Aparece la columna de neuronas de entrada (784) con una flecha desde la cuadrícula.]`

Veamos en concreto qué hace cada capa de una CNN, usando el dígito **ocho** como ejemplo.

En la **capa de entrada**, cada píxel se convierte en una neurona con un valor entre 0 y 1. Para una imagen real de 28x28 píxeles, serían 784 neuronas de entrada.

---

### Acto 2 — Detectores de Bordes *(~15 seg)*

`[PANTALLA: "Detectores de Bordes" en amarillo. Aparece la primera capa oculta (128 neuronas). La cámara hace zoom a una neurona específica y muestra una mini-cuadrícula: borde horizontal. Luego zoom a otra: borde vertical. Luego: curva/diagonal. La cámara vuelve. Texto abajo: "Capa 1: solo detecta bordes y esquinas, no el número completo".]`

La **primera capa oculta** no "ve" el número 8. Solo detecta fragmentos: bordes horizontales, bordes verticales, curvas y diagonales.

*(durante el zoom)*

Esta neurona específica se activa ante bordes **horizontales**. Esta otra, ante **verticales**. Esta, ante **curvas en diagonal**.

Es la misma lógica que su corteza visual primaria: primero, los elementos más simples.

---

### Acto 3 — Detectores de Formas *(~15 seg)*

`[PANTALLA: "Detectores de Formas" en naranja. Aparece la segunda capa oculta (64 neuronas). Se muestra el dígito 8 con sus dos bucles. Una neurona naranja activa detecta el bucle superior con una flecha. Una neurona amarilla detecta el bucle inferior.]`

La **segunda capa oculta** combina los bordes detectados antes para reconocer **formas completas**.

*(durante las flechas)*

Esta neurona se especializa en el **bucle superior** del 8. Esta otra, en el **bucle inferior**. El número 8 tiene exactamente dos de ellos — y la red ya lo sabe.

Así es como las capas construyen una comprensión **jerárquica**: de píxeles a bordes, de bordes a formas, de formas a conceptos.

---

### Acto 4 — Capa de Salida Softmax *(~12 seg)*

`[PANTALLA: "Capa de Salida" en verde. Aparecen 10 neuronas numeradas del 0 al 9. Líneas amarillas brillantes conectan las neuronas de "bucles" con el nodo 8. Las probabilidades aparecen: 98% para el 8, casi 0% para el resto. El nodo 8 hace flash.]`

Y finalmente, la **capa de salida**. La función Softmax convierte todas las activaciones en probabilidades que suman el 100%.

*(cuando el 8 hace flash)*

El resultado: **98% de probabilidad de que sea un ocho**. La decisión está tomada.

En medicina, en lugar de dígitos, esto se traduce a: ¿hay tumor o no? ¿Es benigno o maligno? ¿Qué tan severo?

---

---

## ESCENA 5 — CADe vs CADx + ImageNet `S05_ImageNet_CAD`

---

### Bloque 1 — CADe vs CADx *(~18 seg)*

`[PANTALLA: Título "CADe vs CADx: Detectar vs Diagnosticar". Línea divisora central. Izquierda: "CADe" en amarillo — aparece una radiografía simulada, una línea de escaneo barre la imagen, el bounding box amarillo aparece sobre el nódulo: "Nódulo detectado". Texto: "Objetivo: reducir falsos negativos". Derecha: "CADx" en teal — la misma radiografía ya con el nódulo marcado en teal, barras de probabilidad: Benigno 15% / Maligno 85%.]`

En el entorno clínico existen **dos tipos** de sistemas asistidos por computadora, y es importante no confundirlos.

El **CADe** — Detección Asistida — tiene un solo trabajo: *encontrar* la anomalía. Localizar el nódulo, la lesión, la sombra sospechosa. Su métrica clave es no dejar pasar nada — reducir los **falsos negativos**.

*(señalar derecha)*

El **CADx** — Diagnóstico Asistido — va un paso más allá. Ya sabe dónde está la anomalía; ahora la evalúa: ¿qué tan probable es que sea maligna? ¿Qué tipo de lesión es? ¿Qué tan avanzada está?

*(señalar las barras)*

En este caso: 85% de probabilidad maligna. Eso ya es una señal de alerta crítica para el radiólogo.

---

### Bloque 2 — ImageNet *(~15 seg)*

`[PANTALLA: Transición al nuevo título "ImageNet: La Base de Datos que Cambió Todo". Aparece una cuadrícula de 12 tarjetas de categorías: Perro, Gato, Avión, Silla... Estadísticas: "1.2M imágenes · 1000 categorías". Badge naranja al final: "AlexNet — 2012 · Gana ImageNet con CNN profunda".]`

Ahora bien: ¿de dónde sacan sus datos estas redes para aprender?

La respuesta está en **ImageNet**: la base de datos más grande del mundo para entrenamiento, con **1.2 millones de imágenes** clasificadas en 1000 categorías.

*(durante las tarjetas)*

Perros, gatos, aviones, sillas... Nada que ver con medicina. Pero esto es crucial.

*(señalar el badge de AlexNet)*

En **2012**, AlexNet ganó la competición ImageNet con una distancia tan pronunciada sobre sus rivales que demostró algo fundamental: las CNN podían aprender a reconocer el mundo visual. Y si podían aprender a reconocer 1000 objetos cotidianos — también podían aprender a reconocer patologías.

---

---

## ESCENA 5B — TRANSFER LEARNING `S05b_TransferLearning`

---

### *(~18 seg)*

`[PANTALLA: "Transfer Learning". Caja izquierda azul: "Dominio Fuente — ImageNet 1.2M imágenes" con cuadrícula de fotos naturales. Flecha teal con badge "Transfer Learning". Caja derecha teal: "Dominio Destino — Imágenes Médicas ~500 muestras" con cuadrícula de RX, MRI, Dermatología, Retina, Histología, TC. Caption: "Una red entrenada en millones de imágenes genéricas se adapta a tareas médicas con muy pocos datos".]`

¿Pero cómo se entrena una CNN para medicina si hay muy pocos datos médicos etiquetados?

La respuesta es **transferencia de aprendizaje**.

*(señalar caja izquierda)*

Se toma una red que ya fue entrenada con millones de imágenes de ImageNet. Esta red ya aprendió a detectar bordes, texturas, formas, patrones generales de cualquier imagen visual.

*(señalar la flecha)*

Y entonces se **readapta** ese conocimiento al dominio médico: radiografías de tórax, resonancias, dermoscopía, tomografías...

*(señalar caja derecha)*

Con apenas unos **500 ejemplos médicos** etiquetados — algo que antes era imposible de usar — la red logra un rendimiento clínico robusto. Esto ahorra tiempo, dinero computacional, y resuelve el gran problema de la escasez de datos en medicina.

---

---

## ESCENA 6 — ARQUITECTURAS `S06_Arquitecturas`

---

### AlexNet — Clasificación *(~15 seg)*

`[PANTALLA: "Arquitecturas Clave en Diagnóstico Médico". Sub-título: "AlexNet — Clasificación". Aparece la cadena lineal de bloques: Input 224x224 → Conv/Pool → Conv/Pool → Conv/Conv/Pool → FC 4096 → FC 4096 → Softmax 1000. Imagen de entrada (radiografía de tórax). Salida: "Tumor: SI/NO (clasificación)". Texto abajo: "90.2% precisión en clasificación de pulmón".]`

Hablemos de las tres arquitecturas más relevantes en diagnóstico médico.

**AlexNet** es la que inició todo. Su estructura es lineal: la imagen entra, pasa por bloques de convolución y pooling que reducen progresivamente las dimensiones, y llega a capas totalmente conectadas que toman la decisión final.

*(señalar salida)*

Para medicina: ¿esta radiografía de tórax tiene tumor? **Sí o no**. Eso es clasificación. AlexNet alcanza el 90.2% de precisión en clasificación pulmonar.

---

### U-Net — Segmentación *(~18 seg)*

`[PANTALLA: "U-Net — Segmentación". Aparece la estructura en U: encoder baja por la izquierda, cuello de botella, decoder sube por la derecha. Flechas amarillas punteadas horizontales: skip connections. Imagen de entrada (imagen médica). Salida: imagen segmentada con contorno verde de corazón. Texto: "Predicción pixel a pixel — Alto coeficiente Dice en segmentación cardíaca".]`

**U-Net** resuelve un problema completamente diferente. No solo dice "hay tumor" — sino que delimita **exactamente** dónde está, píxel por píxel.

Su arquitectura tiene forma de U: un **encoder** que va comprimiendo la imagen para entender el contexto, y un **decoder** que va reconstruyendo la imagen con la segmentación marcada.

*(señalar las flechas amarillas)*

Lo brillante son las **skip connections** — estas líneas punteadas en amarillo. Conectan el encoder con el decoder en cada nivel, recuperando la información espacial detallada que se habría perdido en el cuello de botella.

El resultado: contornos exactos de órganos, tumores, lesiones. Es el estándar en segmentación médica.

---

### ResNet — Conexiones Residuales *(~18 seg)*

`[PANTALLA: "ResNet — Conexiones Residuales". Bloque residual: x → Conv/BN/ReLU → Conv/BN → suma (+) → y. Arco amarillo por encima: "x (identidad)". Fórmula: y = F(x) + x. Debajo: "Sin skip: gradiente desaparece en redes profundas" (rojo) / "Con skip: redes de 50-150+ capas sin degradación" (verde). Texto: "AUC 93.2% en clasificación de gliomas".]`

AlexNet demostró que más capas daban mejor precisión. Pero cuando los investigadores intentaron hacer redes más profundas — 50, 100, 150 capas — apareció un problema: el **desvanecimiento del gradiente**. La señal de aprendizaje se diluía antes de llegar a las capas iniciales.

**ResNet** resolvió esto con una idea elegante: conectar la entrada directamente a la salida de cada bloque con un camino residual.

*(señalar el arco amarillo)*

En lugar de aprender F(x) desde cero, la red aprende **la diferencia** entre lo que tiene y lo que necesita: y = F(x) + x.

Esto permite entrenar redes de más de 150 capas sin pérdida de precisión. En clasificación de gliomas cerebrales: **AUC de 93.2%**.

---

### Tabla Comparativa *(~8 seg)*

`[PANTALLA: "Comparativa". Tabla de 3 columnas: Arquitectura | Tarea principal | Clave técnica. AlexNet: Clasificación / Capas conv + FC. U-Net: Segmentación / Encoder/Decoder + skip. ResNet: Alta precisión / Conexiones residuales.]`

Para resumir:

- **AlexNet**: responde "¿qué hay en la imagen?"
- **U-Net**: responde "¿dónde está exactamente?"
- **ResNet**: permite ir más profundo sin degradarse.

Cada una resuelve un problema distinto — y en medicina, los tres problemas existen.

---

---

## ESCENA 7 — MÉTRICAS `S07_Metricas`

---

### Acto 1 — El Espejismo de la Precisión *(~18 seg)*

`[PANTALLA: "El Espejismo de la Precisión". Grid de 100 puntos: 99 verdes (sanos) y 1 rojo (enfermo). Un scanner barre de arriba a abajo pintando todo de verde. El número "99%" aparece grande en verde. Luego el punto rojo se amplía al triple. Texto rojo: "Falso Negativo: el tumor que se perdió". El "99%" tiembla y se vuelve rojo. Texto: "Alta precisión NO garantiza detectar enfermos".]`

Ahora debemos hablar de algo crítico: cómo medimos si un modelo realmente funciona. Porque la métrica más intuitiva — la precisión — puede ser **tramposa**.

*(durante el scanner)*

Imaginen un modelo que clasifica a todos los pacientes como sanos. Si en la muestra hay 99 sanos y 1 enfermo, el modelo tendría un 99% de precisión.

*(cuando aparece el punto rojo ampliado)*

Pero **este punto rojo** — el único paciente con tumor — quedó sin detectar.

*(cuando el 99% tiembla)*

Una precisión del 99% ocultó un **100% de fallos** en los casos que realmente importaban.

---

### Acto 2 — Las Dos Balanzas *(~20 seg)*

`[PANTALLA: "Las Dos Balanzas". Divisor central. Izquierda: "Sensibilidad" en verde — fórmula VP / (VP+FN) — puntos rojos (enfermos), 4 rodeados (VP detectados), 2 sin rodear (FN). Derecha: "Especificidad" en teal — fórmula VN / (VN+FP) — puntos verdes (sanos), 2 con círculo rojo (FP). Slider de umbral se mueve: a la izquierda sube sensibilidad / baja especificidad; a la derecha al revés.]`

Por eso usamos **dos métricas complementarias**.

*(señalar izquierda)*

La **Sensibilidad**: de todos los enfermos, ¿cuántos detectó el modelo? Se calcula dividiendo los verdaderos positivos entre verdaderos positivos más falsos negativos. En medicina, una sensibilidad alta significa: no me pierdo a ningún enfermo.

*(señalar derecha)*

La **Especificidad**: de todos los sanos, ¿cuántos identificó correctamente? Si es baja, el modelo alarma a pacientes sanos innecesariamente.

*(durante el slider)*

Y aquí está la tensión clásica: al mover el **umbral de decisión**, ganar sensibilidad cuesta especificidad — y viceversa. Este balance es una decisión clínica, no solo matemática. ¿Prefiero no perder ningún enfermo aunque alarme a más sanos? O ¿prefiero menos falsas alarmas aunque corra el riesgo de perder algún caso?

---

### Acto 3 — Curva ROC *(~18 seg)*

`[PANTALLA: "Curva ROC". Aparecen los ejes: Eje X "1 - Especificidad (Falsas alarmas)" · Eje Y "Sensibilidad (Detectar enfermos)". Línea diagonal gris: "Adivinanza aleatoria". Notas laterales: "Moverse por el eje X = pagar con falsas alarmas" / "Subir en el eje Y = ganar: detectar enfermos". La curva ROC amarilla se dibuja progresivamente. Punto de operación marcado: "78% sensibilidad · 20% falsas alarmas".]`

La **Curva ROC** nos permite visualizar el balance en todos los umbrales posibles a la vez.

*(señalar diagonal gris)*

Esta línea diagonal gris es el modelo más inútil posible: es como lanzar una moneda. Cualquier modelo que sirva debe quedar **por encima** de ella.

*(durante el dibujo de la curva amarilla)*

Cada punto de la curva dice: "si elijo este umbral, pago con X% de falsas alarmas y gano Y% de sensibilidad."

*(señalar punto de operación)*

El radiólogo elige su punto de operación según el contexto clínico: aquí, 78% de sensibilidad pagando un 20% de falsas alarmas.

---

### Acto 4 — El AUC *(~20 seg)*

`[PANTALLA: "La Calificación Final — AUC". Se rellena el área bajo la curva amarilla. El número AUC sube animado de 0 a 0.85. Luego la curva se transforma en la diagonal (AUC 0.50 en rojo): "Modelo inútil". Luego curva ángulo recto (AUC 1.00 en verde): "Modelo perfecto: 100% sens + 100% espec". Vuelve al modelo real: AUC 0.932. Caption: "AUC resume qué tan bien el modelo separa enfermos de sanos a cualquier umbral de decisión".]`

Para reducir todo esto a un **número único**, usamos el AUC — el Área Bajo la Curva ROC.

*(durante la animación del 0.50)*

Un AUC de 0.50: el modelo no sabe nada. Es una moneda al aire.

*(durante el 1.00)*

Un AUC de 1.0: perfección absoluta. 100% de sensibilidad con 0% de falsas alarmas.

*(volviendo al 0.932)*

Los modelos clínicamente validados que hemos revisado alcanzan AUC de **0.932 en gliomas**. El AUC resume, en un solo número, qué tan bien el modelo distingue enfermos de sanos **sin importar qué umbral se elija**.

---

---

## ESCENA 8 — APLICACIONES REALES `S08_Aplicaciones`

---

### Los 5 casos *(~20 seg)*

`[PANTALLA: "Aplicaciones Reales". Aparecen 5 tarjetas una a una:]`
`· Viz.ai · Detección de ACV · AUC > 0.90 · 1,600+ hospitales · −66 min tratamiento`
`· Mirai (MIT) · Riesgo cáncer de mama · C-index 0.69–0.78 · 5 países · Predicción a 5 años`
`· Aidoc · Hemorragia intracraneal · Sens. > 90% · Triaje automático`
`· Qure.ai · Nódulos pulmonares · FDA cleared · Segmentación en CT`
`· Shockmatrix · Triaje en trauma · 1,292 casos · IA y médicos son complementarios`

Estos números no son proyecciones ni laboratorio. Son sistemas que **ya están funcionando en hospitales reales**.

*(tarjeta 1 — Viz.ai)*

**Viz.ai** desplegado en más de 1,600 hospitales, detecta oclusiones de grandes vasos para prevenir accidentes cerebrovasculares con un AUC superior a 0.90. El resultado clínico más impactante: **reducción de 66 minutos** en el tiempo de inicio del tratamiento. En un ACV, cada minuto destruye neuronas.

*(tarjeta 2 — Mirai)*

**Mirai**, del MIT, predice si una paciente va a desarrollar cáncer de mama en los próximos **5 años**, solo con una mamografía. Validado en 5 países. Permite personalizar cuándo debe hacerse la próxima revisión según el riesgo individual de cada paciente.

*(tarjeta 3 — Aidoc)*

**Aidoc** detecta hemorragia intracraneal con sensibilidad superior al 90%. Opera como triaje automático: el sistema prioriza qué caso debe ver primero el radiólogo.

*(tarjeta 4 — Qure.ai)*

**Qure.ai** detecta y segmenta nódulos pulmonares en tomografías. Autorizado por la FDA. Útil para cribado de cáncer de pulmón a gran escala.

*(tarjeta 5 — Shockmatrix)*

Y este es el más revelador: **Shockmatrix**, en un ensayo con 1,292 casos de trauma en Francia, la IA falló en 20 pacientes que los médicos detectaron — pero los médicos fallaron en 21 que la IA identificó. **Son complementarios**. Ni la IA reemplaza al médico, ni el médico hace innecesaria la IA.

---

### Impacto Clínico *(~15 seg)*

`[PANTALLA: "Impacto Clínico". Aparecen 5 ítems uno a uno: Triaje en tiempo real · Reducción de 66 min en ACV · Detección complementaria · Cribado personalizado · 873 algoritmos FDA autorizados (2025)]`

El patrón de impacto es claro:

La IA no reemplaza al radiólogo — lo **empodera**. Le da velocidad en los casos urgentes, cobertura en los casos que podría perder, y personalización que antes era imposible a escala.

**873 algoritmos** autorizados en radiología. El mercado no está especulando: ya está desplegando.

---

---

## ESCENA 9 — LIMITACIONES Y DESAFÍOS ÉTICOS `S09_Limitaciones`

---

### Limitación 1 — Sesgo y Generalización *(~12 seg)*

`[PANTALLA: "Limitaciones y Desafíos". Sub-título "1. Sesgo y Generalización". Dos tarjetas: Hospital A (verde) "95% precisión — mismo equipo y población del training" → flecha amarilla "−15%" → Hospital B (rojo) "~80% precisión — distinto equipo, población diferente".]`

Ahora lo que el entusiasmo no debe ocultar: los **desafíos reales**.

El primero es el **sesgo**. Un modelo entrenado en un hospital, con una población predominantemente caucásica y equipos específicos, puede caer **15 puntos porcentuales** de precisión cuando se despliega en otro hospital con diferente demografía o diferente escáner.

Si los datos de entrenamiento no son diversos, el modelo reproduce y amplifica las desigualdades del sistema de salud.

---

### Limitación 2 — Caja Negra + XAI *(~12 seg)*

`[PANTALLA: "2. Interpretabilidad — Caja Negra". Rectángulo negro con un "?" gigante. Flecha azul con "Imagen" entra. Flecha verde con "Maligno 94.7%" sale. Texto: "XAI (Grad-CAM, SHAP) intenta explicar, pero radiólogos lo encuentran insuficiente".]`

El segundo desafío es el más profundo filosóficamente: la **caja negra**.

*(señalar el signo de interrogación)*

La CNN toma una imagen, procesa millones de parámetros que nadie entiende completamente, y dice "94.7% de probabilidad maligna". ¿Pero **por qué**? ¿Qué vio exactamente?

Los métodos de IA explicable — Grad-CAM, SHAP — generan mapas de calor que muestran qué regiones activaron la decisión. Pero los radiólogos frecuentemente los encuentran insuficientes para confiar en un diagnóstico tan sensible como un tumor cerebral.

Sin explicabilidad, la confianza clínica no puede consolidarse.

---

### Limitaciones 3–6 — Desafíos Adicionales *(~15 seg)*

`[PANTALLA: "Desafíos Adicionales". Aparecen 4 tarjetas en cuadrícula: Regulación · Responsabilidad · Integración · Escalabilidad. Al final, cuadro teal: "La IA es un copiloto, no un reemplazo del especialista".]`

Los desafíos restantes son igual de reales:

*(tarjeta Regulación)*

**Regulación**: la FDA aprueba versiones estáticas. Si el modelo se actualiza con nuevos datos — requiere una nueva autorización completa. Eso frena la mejora continua.

*(tarjeta Responsabilidad)*

**Responsabilidad**: si la IA comete un error y el radiólogo lo firmó, ¿quién responde? En la mayoría de jurisdicciones: el médico. Eso genera cautela en la adopción.

*(tarjeta Integración)*

**Integración**: los sistemas hospitalarios legacy — PACS, RIS — no fueron diseñados para recibir IA. Integrarlos es técnicamente complejo y costoso.

*(tarjeta Escalabilidad)*

**Escalabilidad**: entrenar estas redes requiere GPUs costosas y etiquetado por expertos. Para una clínica pequeña en un país en desarrollo, es prohibitivo.

*(señalar cuadro final teal)*

Y la conclusión que resume todo: **la IA es un copiloto, no un reemplazo del especialista**. Su valor está en la colaboración humano-máquina, no en la sustitución.

---

---

## ESCENA 10 — CONCLUSIONES `S10_Conclusiones`

---

### Síntesis de hallazgos *(~15 seg)*

`[PANTALLA: "Conclusiones". Aparecen 5 ítems uno a uno: AUC 93.2% gliomas · Sens. > 90% hemorragia · U-Net estándar segmentación · 873 algoritmos FDA 2025 · Adopción plena: solo 2% en EE.UU.]`

Los números son claros. Las CNN han demostrado eficacia clínica **comprobada**:

AUC de 93.2% en gliomas. 89.6% en cáncer de mama. Sensibilidad superior al 90% en hemorragias. U-Net como estándar de segmentación. 873 algoritmos ya autorizados.

*(pausa, señalar el último punto)*

Pero solo el **2% de los hospitales en EE.UU.** ha implementado esto plenamente. La brecha entre lo que la ciencia puede hacer y lo que la clínica usa — sigue siendo enorme. Ese es el desafío real del próximo decenio.

---

### Perspectivas Futuras *(~15 seg)*

`[PANTALLA: "Perspectivas Futuras". Aparecen 4 ítems con flecha "→": XAI · Modelos multimodales · IA Adaptativa · Aprendizaje Federado]`

¿Hacia dónde va esto?

**IA Explicable**: herramientas que no solo diagnostican sino que muestran *por qué* — para que el médico pueda confiar y validar.

**Modelos Multimodales**: integrar la imagen con el historial clínico completo del paciente, sus análisis de laboratorio, sus antecedentes. Un diagnóstico transversal, no fragmentado.

**IA Adaptativa**: marcos regulatorios que permitan que los modelos mejoren continuamente sin necesidad de empezar desde cero en cada actualización.

**Aprendizaje Federado**: que hospitales en diferentes países puedan entrenar modelos juntos **sin compartir datos privados de pacientes**. Colaboración sin vulnerar la privacidad.

---

### Galería de Imágenes Reales *(~25 seg)*

`[PANTALLA: "Imágenes Reales del Dominio". Aparecen 10 imágenes en secuencia con transición lateral: MRI cerebral · Segmentación de tumor · Radiología digital · Capas de CNN · Arquitectura U-Net · Neurona artificial · Diagnóstico dental · Tomografía abdominal · Ejemplo de clasificación · Portada IA en Diagnóstico Médico.]`

*(silencio o música suave — dejar que las imágenes hablen)*

*(opcional, voz pausada)*

Esto no es ciencia ficción. No es el futuro. Es lo que existe hoy en clínicas y hospitales del mundo. Imágenes que una máquina aprende a leer — para que ningún diagnóstico llegue demasiado tarde.

---

### Cierre Final *(~10 seg)*

`[PANTALLA: Fade a negro. Silencio.]`

*(pausar un momento antes de hablar)*

La inteligencia artificial no reemplaza la intuición clínica, la empatía, ni el criterio del especialista. Pero sí puede ser el par de ojos que nunca se cansa, que no tiene sesgo de fatiga, y que puede revisar mil imágenes mientras el médico duerme.

El objetivo no es una IA que diagnostique sola. El objetivo es **un médico mejor equipado** gracias a la IA.

*(pausa final)*

Eso es todo. Quedo abierto a preguntas.

---

---

## GUÍA DE TIMING ESTIMADO

| Escena | Nombre                        | Duración video | Tiempo narración |
|--------|-------------------------------|----------------|------------------|
| S01    | Portada                       | ~20 seg        | ~15 seg          |
| S02    | Introducción                  | ~30 seg        | ~35 seg          |
| S03    | ANN vs CNN                    | ~25 seg        | ~30 seg          |
| S04    | Capas de CNN                  | ~40 seg        | ~50 seg          |
| S05    | CADe vs CADx + ImageNet       | ~35 seg        | ~40 seg          |
| S05b   | Transfer Learning             | ~25 seg        | ~25 seg          |
| S06    | Arquitecturas                 | ~50 seg        | ~60 seg          |
| S07    | Métricas                      | ~70 seg        | ~80 seg          |
| S08    | Aplicaciones Reales           | ~40 seg        | ~50 seg          |
| S09    | Limitaciones y Desafíos       | ~35 seg        | ~45 seg          |
| S10    | Conclusiones + Galería        | ~50 seg        | ~55 seg          |
| **TOTAL** |                           | **~7 min**     | **~8 min**       |

---

## NOTAS DE PRESENTACIÓN

- **Velocidad óptima**: habla más lento de lo que crees necesario. 130 palabras/minuto es ideal para material técnico.
- **Durante transiciones de animación**: deja siempre 1-2 segundos de silencio para que la imagen "respire" antes de explicarla.
- **Puntos de contacto visual**: mira a la audiencia en las frases de cierre de cada sección, no a la pantalla.
- **La galería final (S10)**: es el único momento donde el silencio es la mejor narración. Deja que las imágenes reales generen el impacto emocional.
- **Frases gancho para retomar si te pierdes**: "Lo que vemos aquí es..." / "Lo importante de esto es..." / "En términos clínicos, esto significa..."
- **Si te preguntan sobre los datos**: AUC 93.2% → gliomas (ResNet). AUC 0.90+ → Viz.ai. Sensibilidad > 90% → Aidoc. C-index 0.69–0.78 → Mirai (MIT). Fuente: Laurent, 2025.
