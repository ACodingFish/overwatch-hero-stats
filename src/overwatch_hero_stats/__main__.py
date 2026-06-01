from .app_main import main_app
import uvicorn

main_app.start()
uvicorn.run("overwatch_hero_stats.api_main:app", host="0.0.0.0", port=8000, reload=True)