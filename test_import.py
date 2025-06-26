try:
    import aiogram
    import dotenv
    print("✅ All imports work!")
except ImportError as e:
    print(f"❌ Import error: {e}")
    raise
