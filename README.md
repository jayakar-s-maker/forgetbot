**ForgetBot**

A smart mirror that recognizes who you are on approach and verbally reminds you what to pack based on where you're headed.

<img width="597" height="335" alt="ForgetBot Mockup" src="https://github.com/user-attachments/assets/7ebe43dc-0d31-4c41-94df-db32459e9778" />

*(Concept render of the physical 3" shadow box enclosure layout)*

---

### 🌟 What It Does
* **Smart Departure Reminders:** Walk up to the mirror, and it recognizes your face and asks where you're headed. Say *"I'm going shopping,"* and it tells you exactly what to bring.
* **MagicMirror Dashboard:** Displays live weather, news, and streams background music while idle.
* **Hands-Free Audio:** Fully interactive voice commands via an integrated USB microphone and mini speaker.

---

### 🛠️ Hardware & Components (Bill of Materials)

| Component | Purpose | Status |
| :--- | :--- | :--- |
| **Raspberry Pi 5** | Main computing board for MagicMirror UI & audio processing | Need Funding |
| **Raspberry Pi AI Camera** | Onboard NPU face detection | Need Funding |
| **3" Deep Shadow Box** | Custom physical enclosure housing Pi 5, screen, and wiring | Need Funding |
| **USB Microphone** | Voice command input | Need Funding |
| **Mini USB Speaker** | Voice prompt output | Need Funding |
| **Active Cooler** | Pi 5 thermal management | Need Funding |

> 📄 *Full component list, cost breakdown, and part links are available in [`BOM.csv`](./BOM.csv).*

---

### 🔌 How It Works (Hardware & Architecture)

Offloading face detection directly to the **Raspberry Pi AI Camera’s neural processing unit (NPU)** keeps the Raspberry Pi 5 CPU free. This ensures the MagicMirror display stays smooth and lag-free while running background audio and voice processing.

#### Enclosure & Layout:
All components are mounted inside a **3" deep shadow box frame**, providing adequate clearance for:
1. The Raspberry Pi 5 with its Active Cooler.
2. Routing internal USB cables for the speaker and microphone.
3. Display driver boards and power routing behind the mirror glass.

---

### 📁 Repository Layout
```text
├── cad/         <-- Enclosure dimensions and CAD assembly files
├── wiring/      <-- Connection and wiring diagrams
├── software/    <-- MagicMirror modules and python backend
└── BOM.csv      <-- Complete Bill of Materials and hardware budget
 
