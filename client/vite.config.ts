import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server:{
    port: 3000,
    host: true,
    hmr:{
      host: '0.0.0.0',
      clientPort: 3000,
    },
    watch:{
      usePolling: true,
    },
  },
})
