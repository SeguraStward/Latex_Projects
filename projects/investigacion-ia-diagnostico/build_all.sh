#!/bin/bash
set -e
trap 'echo "Error compiling"; exit 1' ERR

echo "Compilando todas las escenas de Manim en Alta Calidad (1080p60)..."

cd "$(dirname "$0")/../.."
echo "Working directory: $PWD"

SCENES=("S01_Portada" "S02_Introduccion" "S03_ANN_CNN" "S04_CapasCNN" "S05_ImageNet_CAD" "S05b_TransferLearning" "S06_Arquitecturas" "S07_Metricas" "S08_Aplicaciones" "S09_Limitaciones" "S10_Conclusiones")

for scene in "${SCENES[@]}"; do
    echo "=== Compilando $scene ==="
    ./compile.sh investigacion-ia-diagnostico manim-hq "$scene"
done

echo "=== Concatenando el video completo con ffmpeg ==="
cd projects/investigacion-ia-diagnostico/animations/media/videos

rm -f concat.txt
for dir in s01_portada s02_introduccion s03_ann_cnn s04_capas_cnn s05_imagenet_cad s05b_transfer_learning s06_arquitecturas s07_metricas s08_aplicaciones s09_limitaciones s10_conclusiones; do
    video=$(ls "$dir/1080p60/"*.mp4 2>/dev/null | sort | head -n 1 || true)
    if [ -n "$video" ]; then
        echo "file '$PWD/$video'" >> concat.txt
    fi
done

ffmpeg -y -f concat -safe 0 -i concat.txt -c copy ../../../presentacion_completa.mp4
echo "=== ¡Video completo generado exitosamente en projects/investigacion-ia-diagnostico/presentacion_completa.mp4! ==="
