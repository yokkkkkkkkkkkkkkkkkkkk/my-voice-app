[app]
title = My Voice App
package.name = myvoiceapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.2.1,kivymd==1.1.1,sdl2_ttf==2.20.2
orientation = portrait
android.permissions = RECORD_AUDIO, INTERNET, WRITE_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
