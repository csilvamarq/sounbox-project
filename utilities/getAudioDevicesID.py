import pyaudio

# Inicializar PyAudio
p = pyaudio.PyAudio()

# Obtener el número de dispositivos de audio disponibles
num_devices = p.get_device_count()

# Imprimir la información de cada dispositivo de audio
for i in range(num_devices):
    device_info = p.get_device_info_by_index(i)
    print(f"Device {i}: {device_info['name']}, {device_info['hostApi']}, {device_info['maxInputChannels']} input channels, {device_info['maxOutputChannels']} output channels")