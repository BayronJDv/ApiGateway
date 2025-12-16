# API Gateway

API Gateway que actúa como punto de entrada centralizado para rutas protegidas. Utiliza Supabase para autenticación y valida tokens JWT en los headers de las solicitudes.

## Requisitos

- Python 3.8+
- pip

## Instalación

1. Clona el repositorio:
```bash
git clone <url-del-repositorio>
cd Apigateway
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Crea un archivo `.env` con tus credenciales de Supabase:
```env
VITE_SUPABASE_URL=tu_url_supabase
VITE_SUPABASE_ANON_KEY=tu_anon_key
```

## Inicio rápido

Ejecuta el servidor:
```bash
fastapi dev main.py
```

El servidor estará disponible en `http://localhost:8000`

## Rutas disponibles

- `GET /example` - Acceso protegido. Requiere header `Authorization: Bearer <token>`
