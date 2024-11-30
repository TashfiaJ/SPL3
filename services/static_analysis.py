from androguard.core.bytecodes.apk import APK

def perform_static_analysis(apk_path):
    try:
        # Load the APK using Androguard
        app = APK(apk_path)

        # Extract APK information
        package_name = app.get_package()
        permissions = app.get_permissions()
        activities = app.get_activities()
        urls = app.get_urls()  # Extract URLs from the APK

        return {
            "package_name": package_name,
            "permissions": permissions,
            "activities": activities,
            "urls": urls
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
