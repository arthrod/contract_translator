Project Path: bilingual_book_maker

Source Tree:

```
bilingual_book_maker
├── typos.toml
├── book_maker
│   ├── config.py
│   ├── obok.py
│   ├── __init__.py
│   ├── translator
│   │   ├── base_translator.py
│   │   ├── chatgptapi_translator.py
│   │   ├── google_translator.py
│   │   ├── deepl_free_translator.py
│   │   ├── caiyun_translator.py
│   │   ├── groq_translator.py
│   │   ├── __init__.py
│   │   ├── custom_api_translator.py
│   │   ├── claude_translator.py
│   │   ├── tencent_transmart_translator.py
│   │   ├── deepl_translator.py
│   │   ├── xai_translator.py
│   │   ├── gemini_translator.py
│   │   └── litellm_translator.py
│   ├── cli.py
│   ├── utils.py
│   ├── loader
│   │   ├── srt_loader.py
│   │   ├── __init__.py
│   │   ├── txt_loader.py
│   │   ├── md_loader.py
│   │   ├── base_loader.py
│   │   ├── helper.py
│   │   └── epub_loader.py
│   └── __main__.py
├── mkdocs.yml
├── LICENSE
├── Dockerfile
├── Makefile
├── pyproject.toml
├── tests
│   └── test_integration.py
├── docs
└── make_book.py

```

`/Users/arthrod/Library/CloudStorage/GoogleDrive-arthursrodrigues@gmail.com/My Drive/acode/atemp-drive/bilingual_book_maker/typos.toml`:

```toml
   1 | # See https://github.com/crate-ci/typos/blob/master/docs/reference.md to configure typos
   2 | [default.extend-words]
   3 | sur = "sur"
   4 | banch = "banch" # TODO: not sure if this is a typo or not
   5 | fo = "fo"
   6 | ba = "ba"
   7 | [files]
   8 | extend-exclude = ["LICENSE"]

```

`/Users/arthrod/Library/CloudStorage/GoogleDrive-arthursrodrigues@gmail.com/My Drive/acode/atemp-drive/bilingual_book_maker/book_maker/config.py`:

```py
   1 | config = {
   2 |     "translator": {
   3 |         "chatgptapi": {
   4 |             "context_paragraph_limit": 3,
   5 |             "batch_context_update_interval": 50,
   6 |         }
   7 |     },
   8 | }

```

`/Users/arthrod/Library/CloudStorage/GoogleDrive-arthursrodrigues@gmail.com/My Drive/acode/atemp-drive/bilingual_book_maker/book_maker/obok.py`:

```py
   1 | # The original code comes from:
   2 | # https://github.com/apprenticeharper/DeDRM_tools
   3 | 
   4 | # Version 4.1.2 March 2023
   5 | # Update library for crypto for current Windows
   6 | 
   7 | # Version 4.1.1 March 2023
   8 | # Make obok.py works as file selector
   9 | 
  10 | # Version 4.1.0 February 2021
  11 | # Add detection for Kobo directory location on Linux
  12 | 
  13 | # Version 4.0.0 September 2020
  14 | # Python 3.0
  15 | #
  16 | # Version 3.2.5 December 2016
  17 | # Improve detection of good text decryption.
  18 | #
  19 | # Version 3.2.4 December 2016
  20 | # Remove incorrect support for Kobo Desktop under Wine
  21 | #
  22 | # Version 3.2.3 October 2016
  23 | # Fix for windows network user and more xml fixes
  24 | #
  25 | # Version 3.2.2 October 2016
  26 | # Change to the way the new database version is handled.
  27 | #
  28 | # Version 3.2.1 September 2016
  29 | # Update for v4.0 of Windows Desktop app.
  30 | #
  31 | # Version 3.2.0 January 2016
  32 | # Update for latest version of Windows Desktop app.
  33 | # Support Kobo devices in the command line version.
  34 | #
  35 | # Version 3.1.9 November 2015
  36 | # Handle Kobo Desktop under wine on Linux
  37 | #
  38 | # Version 3.1.8 November 2015
  39 | # Handle the case of Kobo Arc or Vox device (i.e. don't crash).
  40 | #
  41 | # Version 3.1.7 October 2015
  42 | # Handle the case of no device or database more gracefully.
  43 | #
  44 | # Version 3.1.6 September 2015
  45 | # Enable support for Kobo devices
  46 | # More character encoding fixes (unicode strings)
  47 | #
  48 | # Version 3.1.5 September 2015
  49 | # Removed requirement that a purchase has been made.
  50 | # Also add in character encoding fixes
  51 | #
  52 | # Version 3.1.4 September 2015
  53 | # Updated for version 3.17 of the Windows Desktop app.
  54 | #
  55 | # Version 3.1.3 August 2015
  56 | # Add translations for Portuguese and Arabic
  57 | #
  58 | # Version 3.1.2 January 2015
  59 | # Add coding, version number and version announcement
  60 | #
  61 | # Version 3.05 October 2014
  62 | # Identifies DRM-free books in the dialog
  63 | #
  64 | # Version 3.04 September 2014
  65 | # Handles DRM-free books as well (sometimes Kobo Library doesn't
  66 | # show download link for DRM-free books)
  67 | #
  68 | # Version 3.03 August 2014
  69 | # If PyCrypto is unavailable try to use libcrypto for AES_ECB.
  70 | #
  71 | # Version 3.02 August 2014
  72 | # Relax checking of application/xhtml+xml  and image/jpeg content.
  73 | #
  74 | # Version 3.01 June 2014
  75 | # Check image/jpeg as well as application/xhtml+xml content. Fix typo
  76 | # in Windows ipconfig parsing.
  77 | #
  78 | # Version 3.0 June 2014
  79 | # Made portable for Mac and Windows, and the only module dependency
  80 | # not part of python core is PyCrypto. Major code cleanup/rewrite.
  81 | # No longer tries the first MAC address; tries them all if it detects
  82 | # the decryption failed.
  83 | #
  84 | # Updated September 2013 by Anon
  85 | # Version 2.02
  86 | # Incorporated minor fixes posted at Apprentice Alf's.
  87 | #
  88 | # Updates July 2012 by Michael Newton
  89 | # PWSD ID is no longer a MAC address, but should always
  90 | # be stored in the registry. Script now works with OS X
  91 | # and checks plist for values instead of registry. Must
  92 | # have biplist installed for OS X support.
  93 | #
  94 | # Original comments left below; note the "AUTOPSY" is inaccurate. See
  95 | # KoboLibrary.userkeys and KoboFile.decrypt()
  96 | #
  97 | ##########################################################
  98 | #                    KOBO DRM CRACK BY                   #
  99 | #                      PHYSISTICATED                     #
 100 | ##########################################################
 101 | # This app was made for Python 2.7 on Windows 32-bit
 102 | #
 103 | # This app needs pycrypto - get from here:
 104 | # http://www.voidspace.org.uk/python/modules.shtml
 105 | #
 106 | # Usage: obok.py
 107 | # Choose the book you want to decrypt
 108 | #
 109 | # Shouts to my krew - you know who you are - and one in
 110 | # particular who gave me a lot of help with this - thank
 111 | # you so much!
 112 | #
 113 | # Kopimi /K\
 114 | # Keep sharing, keep copying, but remember that nothing is
 115 | # for free - make sure you compensate your favorite
 116 | # authors - and cut out the middle man whenever possible
 117 | # ;) ;) ;)
 118 | #
 119 | # DRM AUTOPSY
 120 | # The Kobo DRM was incredibly easy to crack, but it took
 121 | # me months to get around to making this. Here's the
 122 | # basics of how it works:
 123 | # 1: Get MAC address of first NIC in ipconfig (sometimes
 124 | # stored in registry as pwsdid)
 125 | # 2: Get user ID (stored in tons of places, this gets it
 126 | # from HKEY_CURRENT_USER\Software\Kobo\Kobo Desktop
 127 | # Edition\Browser\cookies)
 128 | # 3: Concatenate and SHA256, take the second half - this
 129 | # is your master key
 130 | # 4: Open %LOCALAPPDATA%\Kobo Desktop Editions\Kobo.sqlite
 131 | # and dump content_keys
 132 | # 5: Unbase64 the keys, then decode these with the master
 133 | # key - these are your page keys
 134 | # 6: Unzip EPUB of your choice, decrypt each page with its
 135 | # page key, then zip back up again
 136 | #
 137 | # WHY USE THIS WHEN INEPT WORKS FINE? (adobe DRM stripper)
 138 | # Inept works very well, but authors on Kobo can choose
 139 | # what DRM they want to use - and some have chosen not to
 140 | # let people download them with Adobe Digital Editions -
 141 | # they would rather lock you into a single platform.
 142 | #
 143 | # With Obok, you can sync Kobo Desktop, decrypt all your
 144 | # ebooks, and then use them on whatever device you want
 145 | # - you bought them, you own them, you can do what you
 146 | # like with them.
 147 | #
 148 | # Obok is Kobo backwards, but it is also means "next to"
 149 | # in Polish.
 150 | # When you buy a real book, it is right next to you. You
 151 | # can read it at home, at work, on a train, you can lend
 152 | # it to a friend, you can scribble on it, and add your own
 153 | # explanations/translations.
 154 | #
 155 | # Obok gives you this power over your ebooks - no longer
 156 | # are you restricted to one device. This allows you to
 157 | # embed foreign fonts into your books, as older Kobo's
 158 | # can't display them properly. You can read your books
 159 | # on your phones, in different PC readers, and different
 160 | # ereader devices. You can share them with your friends
 161 | # too, if you like - you can do that with a real book
 162 | # after all.
 163 | #
 164 | """Manage all Kobo books, either encrypted or DRM-free."""
 165 | 
 166 | __version__ = "4.1.2"
 167 | __about__ = f"Obok v{__version__}\nCopyright © 2012-2020 Physisticated et al."
 168 | 
 169 | import base64
 170 | import binascii
 171 | import contextlib
 172 | import hashlib
 173 | import os
 174 | import re
 175 | import shutil
 176 | import sqlite3
 177 | import subprocess
 178 | import sys
 179 | import tempfile
 180 | import xml.etree.ElementTree as ET
 181 | import zipfile
 182 | 
 183 | can_parse_xml = True
 184 | try:
 185 |     from xml.etree import ElementTree as ET
 186 | 
 187 |     # print "using xml.etree for xml parsing"
 188 | except ImportError:
 189 |     can_parse_xml = False
 190 |     # print "Cannot find xml.etree, disabling extraction of serial numbers"
 191 | 
 192 | # List of all known hash keys
 193 | KOBO_HASH_KEYS = ["88b3a2e13", "XzUhGYdFp", "NoCanLook", "QJhwzAtXL"]
 194 | 
 195 | 
 196 | class ENCRYPTIONError(Exception):
 197 |     pass
 198 | 
 199 | 
 200 | def _load_crypto_libcrypto():
 201 |     from ctypes import (
 202 |         CDLL,
 203 |         POINTER,
 204 |         Structure,
 205 |         c_char_p,
 206 |         c_int,
 207 |         c_long,
 208 |         create_string_buffer,
 209 |     )
 210 |     from ctypes.util import find_library
 211 | 
 212 |     if sys.platform.startswith("win"):
 213 |         libcrypto = find_library("libcrypto")
 214 |     else:
 215 |         libcrypto = find_library("crypto")
 216 | 
 217 |     if libcrypto is None:
 218 |         raise ENCRYPTIONError("libcrypto not found")
 219 |     libcrypto = CDLL(libcrypto)
 220 | 
 221 |     AES_MAXNR = 14
 222 | 
 223 |     POINTER(c_char_p)
 224 |     POINTER(c_int)
 225 | 
 226 |     class AES_KEY(Structure):
 227 |         _fields_ = [("rd_key", c_long * (4 * (AES_MAXNR + 1))), ("rounds", c_int)]
 228 | 
 229 |     AES_KEY_p = POINTER(AES_KEY)
 230 | 
 231 |     def F(restype, name, argtypes):
 232 |         func = getattr(libcrypto, name)
 233 |         func.restype = restype
 234 |         func.argtypes = argtypes
 235 |         return func
 236 | 
 237 |     AES_set_decrypt_key = F(c_int, "AES_set_decrypt_key", [c_char_p, c_int, AES_KEY_p])
 238 |     AES_ecb_encrypt = F(None, "AES_ecb_encrypt", [c_char_p, c_char_p, AES_KEY_p, c_int])
 239 | 
 240 |     class AES:
 241 |         def __init__(self, userkey) -> None:
 242 |             self._blocksize = len(userkey)
 243 |             if self._blocksize not in [16, 24, 32]:
 244 |                 raise ENCRYPTIONError(_("AES improper key used"))
 245 |             key = self._key = AES_KEY()
 246 |             rv = AES_set_decrypt_key(userkey, len(userkey) * 8, key)
 247 |             if rv < 0:
 248 |                 raise ENCRYPTIONError(_("Failed to initialize AES key"))
 249 | 
 250 |         def decrypt(self, data):
 251 |             clear = b""
 252 |             for i in range(0, len(data), 16):
 253 |                 out = create_string_buffer(16)
 254 |                 rv = AES_ecb_encrypt(data[i : i + 16], out, self._key, 0)
 255 |                 if rv == 0:
 256 |                     raise ENCRYPTIONError(_("AES decryption failed"))
 257 |                 clear += out.raw
 258 |             return clear
 259 | 
 260 |     return AES
 261 | 
 262 | 
 263 | def _load_crypto_pycrypto():
 264 |     from Crypto.Cipher import AES as _AES
 265 | 
 266 |     class AES:
 267 |         def __init__(self, key) -> None:
 268 |             self._aes = _AES.new(key, _AES.MODE_ECB)
 269 | 
 270 |         def decrypt(self, data):
 271 |             return self._aes.decrypt(data)
 272 | 
 273 |     return AES
 274 | 
 275 | 
 276 | def _load_crypto():
 277 |     AES = None
 278 |     cryptolist = (_load_crypto_pycrypto, _load_crypto_libcrypto)
 279 |     for loader in cryptolist:
 280 |         with contextlib.suppress(ImportError, ENCRYPTIONError):
 281 |             AES = loader()
 282 |             break
 283 |     return AES
 284 | 
 285 | 
 286 | AES = _load_crypto()
 287 | 
 288 | 
 289 | # Wrap a stream so that output gets flushed immediately
 290 | # and also make sure that any unicode strings get
 291 | # encoded using "replace" before writing them.
 292 | class SafeUnbuffered:
 293 |     def __init__(self, stream) -> None:
 294 |         self.stream = stream
 295 |         self.encoding = stream.encoding
 296 |         if self.encoding is None:
 297 |             self.encoding = "utf-8"
 298 | 
 299 |     def write(self, data):
 300 |         if isinstance(data, str):
 301 |             data = data.encode(self.encoding, "replace")
 302 |         self.stream.buffer.write(data)
 303 |         self.stream.buffer.flush()
 304 | 
 305 |     def __getattr__(self, attr):
 306 |         return getattr(self.stream, attr)
 307 | 
 308 | 
 309 | class KoboLibrary:
 310 |     """The Kobo library.
 311 | 
 312 |     This class represents all the information available from the data
 313 |     written by the Kobo Desktop Edition application, including the list
 314 |     of books, their titles, and the user's encryption key(s)."""
 315 | 
 316 |     def __init__(self, serials=None, device_path=None, desktopkobodir="") -> None:
 317 |         if serials is None:
 318 |             serials = []
 319 |         print(__about__)
 320 |         self.kobodir = ""
 321 |         kobodb = ""
 322 | 
 323 |         # Order of checks
 324 |         # 1. first check if a device_path has been passed in, and whether
 325 |         #    we can find the sqlite db in the respective place
 326 |         # 2. if 1., and we got some serials passed in (from saved
 327 |         #    settings in calibre), just use it
 328 |         # 3. if 1. worked, but we didn't get serials, try to parse them
 329 |         #    from the device, if this didn't work, unset everything
 330 |         # 4. if by now we don't have kobodir set, give up on device and
 331 |         #    try to use the Desktop app.
 332 | 
 333 |         # step 1. check whether this looks like a real device
 334 |         if device_path:
 335 |             # we got a device path
 336 |             self.kobodir = os.path.join(device_path, ".kobo")
 337 |             # devices use KoboReader.sqlite
 338 |             kobodb = os.path.join(self.kobodir, "KoboReader.sqlite")
 339 |             if not os.path.isfile(kobodb):
 340 |                 # device path seems to be wrong, unset it
 341 |                 device_path = ""
 342 |                 self.kobodir = ""
 343 |                 kobodb = ""
 344 | 
 345 |         # step 3. we found a device but didn't get serials, try to get them
 346 |         #
 347 |         # we got a device path but no saved serial
 348 |         # try to get the serial from the device
 349 |         # get serial from device_path/.adobe-digital-editions/device.xml
 350 |         if self.kobodir and len(serials) == 0 and can_parse_xml:
 351 |             # print "get_device_settings - device_path = {0}".format(device_path)
 352 |             devicexml = os.path.join(
 353 |                 device_path,
 354 |                 ".adobe-digital-editions",
 355 |                 "device.xml",
 356 |             )
 357 |             # print "trying to load {0}".format(devicexml)
 358 |             if os.path.exists(devicexml):
 359 |                 # print "trying to parse {0}".format(devicexml)
 360 |                 xmltree = ET.parse(devicexml)
 361 |                 for node in xmltree.iter():
 362 |                     if "deviceSerial" in node.tag:
 363 |                         serial = node.text
 364 |                         # print "found serial {0}".format(serial)
 365 |                         serials.append(serial)
 366 |                         break
 367 |             else:
 368 |                 # print "cannot get serials from device."
 369 |                 device_path = ""
 370 |                 self.kobodir = ""
 371 |                 kobodb = ""
 372 | 
 373 |         if self.kobodir == "":
 374 |             # step 4. we haven't found a device with serials, so try desktop apps
 375 |             if desktopkobodir != "":
 376 |                 self.kobodir = desktopkobodir
 377 | 
 378 |             if self.kobodir == "":
 379 |                 if sys.platform.startswith("win"):
 380 |                     import winreg
 381 | 
 382 |                     if (
 383 |                         sys.getwindowsversion().major > 5
 384 |                         and "LOCALAPPDATA" in os.environ
 385 |                     ):
 386 |                         # Python 2.x does not return unicode env. Use Python 3.x
 387 |                         self.kobodir = winreg.ExpandEnvironmentStrings("%LOCALAPPDATA%")
 388 |                     if self.kobodir == "" and "USERPROFILE" in os.environ:
 389 |                         # Python 2.x does not return unicode env. Use Python 3.x
 390 |                         self.kobodir = os.path.join(
 391 |                             winreg.ExpandEnvironmentStrings("%USERPROFILE%"),
 392 |                             "Local Settings",
 393 |                             "Application Data",
 394 |                         )
 395 |                     self.kobodir = os.path.join(
 396 |                         self.kobodir,
 397 |                         "Kobo",
 398 |                         "Kobo Desktop Edition",
 399 |                     )
 400 |                 elif sys.platform.startswith("darwin"):
 401 |                     self.kobodir = os.path.join(
 402 |                         os.environ["HOME"],
 403 |                         "Library",
 404 |                         "Application Support",
 405 |                         "Kobo",
 406 |                         "Kobo Desktop Edition",
 407 |                     )
 408 |                 elif sys.platform.startswith("linux"):
 409 |                     # sets ~/.config/calibre as the location to store the kobodir location info file and creates this directory if necessary
 410 |                     kobodir_cache_dir = os.path.join(
 411 |                         os.environ["HOME"],
 412 |                         ".config",
 413 |                         "calibre",
 414 |                     )
 415 |                     if not os.path.isdir(kobodir_cache_dir):
 416 |                         os.mkdir(kobodir_cache_dir)
 417 | 
 418 |                     # appends the name of the file we're storing the kobodir location info to the above path
 419 |                     kobodir_cache_file = f"{str(kobodir_cache_dir)}/kobo_location"
 420 | 
 421 |                     """if the above file does not exist, recursively searches from the root
 422 |                     of the filesystem until kobodir is found and stores the location of kobodir
 423 |                     in that file so this loop can be skipped in the future"""
 424 |                     original_stdout = sys.stdout
 425 |                     if not os.path.isfile(kobodir_cache_file):
 426 |                         for root, _dirs, files in os.walk("/"):
 427 |                             for file in files:
 428 |                                 if file == "Kobo.sqlite":
 429 |                                     kobo_linux_path = str(root)
 430 |                                     with open(
 431 |                                         kobodir_cache_file,
 432 |                                         "w",
 433 |                                         encoding="utf-8",
 434 |                                     ) as f:
 435 |                                         sys.stdout = f
 436 |                                         print(kobo_linux_path, end="")
 437 |                                         sys.stdout = original_stdout
 438 | 
 439 |                     f = open(kobodir_cache_file, encoding="utf-8")
 440 |                     self.kobodir = f.read()
 441 | 
 442 |             # desktop versions use Kobo.sqlite
 443 |             kobodb = os.path.join(self.kobodir, "Kobo.sqlite")
 444 |             # check for existence of file
 445 |             if not os.path.isfile(kobodb):
 446 |                 # give up here, we haven't found anything useful
 447 |                 self.kobodir = ""
 448 |                 kobodb = ""
 449 | 
 450 |         if self.kobodir != "":
 451 |             self.bookdir = os.path.join(self.kobodir, "kepub")
 452 |             # make a copy of the database in a temporary file
 453 |             # so we can ensure it's not using WAL logging which sqlite3 can't do.
 454 |             self.newdb = tempfile.NamedTemporaryFile(mode="wb", delete=False)
 455 |             print(self.newdb.name)
 456 |             with open(kobodb, "rb") as olddb:
 457 |                 self.newdb.write(olddb.read(18))
 458 |                 self.newdb.write(b"\x01\x01")
 459 |                 olddb.read(2)
 460 |                 self.newdb.write(olddb.read())
 461 |             self.newdb.close()
 462 |             self.__sqlite = sqlite3.connect(self.newdb.name)
 463 |             self.__cursor = self.__sqlite.cursor()
 464 |             self._userkeys = []
 465 |             self._books = []
 466 |             self._volumeID = []
 467 |             self._serials = serials
 468 | 
 469 |     def close(self):
 470 |         """Closes the database used by the library."""
 471 |         self.__cursor.close()
 472 |         self.__sqlite.close()
 473 |         # delete the temporary copy of the database
 474 |         os.remove(self.newdb.name)
 475 | 
 476 |     @property
 477 |     def userkeys(self):
 478 |         """The list of potential userkeys being used by this library.
 479 |         Only one of these will be valid.
 480 |         """
 481 |         if len(self._userkeys) != 0:
 482 |             return self._userkeys
 483 |         for macaddr in self.__getmacaddrs():
 484 |             self._userkeys.extend(self.__getuserkeys(macaddr))
 485 |         return self._userkeys
 486 | 
 487 |     @property
 488 |     def books(self):
 489 |         """The list of KoboBook objects in the library."""
 490 |         if len(self._books) != 0:
 491 |             return self._books
 492 |         """Drm-ed kepub"""
 493 |         for row in self.__cursor.execute(
 494 |             "SELECT DISTINCT volumeid, Title, Attribution, Series FROM content_keys, content WHERE contentid = volumeid",
 495 |         ):
 496 |             self._books.append(
 497 |                 KoboBook(
 498 |                     row[0],
 499 |                     row[1],
 500 |                     self.__bookfile(row[0]),
 501 |                     "kepub",
 502 |                     self.__cursor,
 503 |                     author=row[2],
 504 |                     series=row[3],
 505 |                 ),
 506 |             )
 507 |             self._volumeID.append(row[0])
 508 |         """Drm-free"""
 509 |         for f in os.listdir(self.bookdir):
 510 |             if f not in self._volumeID:
 511 |                 row = self.__cursor.execute(
 512 |                     "SELECT Title, Attribution, Series FROM content WHERE ContentID = '"
 513 |                     + f
 514 |                     + "'",
 515 |                 ).fetchone()
 516 |                 if row is not None:
 517 |                     fTitle = row[0]
 518 |                     self._books.append(
 519 |                         KoboBook(
 520 |                             f,
 521 |                             fTitle,
 522 |                             self.__bookfile(f),
 523 |                             "drm-free",
 524 |                             self.__cursor,
 525 |                             author=row[1],
 526 |                             series=row[2],
 527 |                         ),
 528 |                     )
 529 |                     self._volumeID.append(f)
 530 |         """Sort"""
 531 |         self._books.sort(key=lambda x: x.title)
 532 |         return self._books
 533 | 
 534 |     def __bookfile(self, volumeid):
 535 |         """The filename needed to open a given book."""
 536 |         return os.path.join(self.kobodir, "kepub", volumeid)
 537 | 
 538 |     def __getmacaddrs(self):
 539 |         """The list of all MAC addresses on this machine."""
 540 |         macaddrs = []
 541 |         if sys.platform.startswith("win"):
 542 |             c = re.compile(
 543 |                 "\\s?(" + "[0-9a-f]{2}[:\\-]" * 5 + "[0-9a-f]{2})(\\s|$)",
 544 |                 re.IGNORECASE,
 545 |             )
 546 |             output = subprocess.Popen(
 547 |                 "wmic nic where PhysicalAdapter=True get MACAddress",
 548 |                 shell=True,
 549 |                 stdout=subprocess.PIPE,
 550 |                 text=True,
 551 |             ).stdout
 552 |             for line in output:
 553 |                 if m := c.search(line):
 554 |                     macaddrs.append(re.sub("-", ":", m[1]).upper())
 555 |         elif sys.platform.startswith("darwin"):
 556 |             c = re.compile(
 557 |                 "\\s(" + "[0-9a-f]{2}:" * 5 + "[0-9a-f]{2})(\\s|$)",
 558 |                 re.IGNORECASE,
 559 |             )
 560 |             output = subprocess.check_output(
 561 |                 "/sbin/ifconfig -a",
 562 |                 shell=True,
 563 |                 encoding="utf-8",
 564 |             )
 565 |             matches = c.findall(output)
 566 |             macaddrs.extend(m[0].upper() for m in matches)
 567 |         else:
 568 |             # probably linux
 569 | 
 570 |             # let's try ip
 571 |             c = re.compile(
 572 |                 "\\s(" + "[0-9a-f]{2}:" * 5 + "[0-9a-f]{2})(\\s|$)",
 573 |                 re.IGNORECASE,
 574 |             )
 575 |             for line in os.popen("ip -br link"):
 576 |                 if m := c.search(line):
 577 |                     macaddrs.append(m[1].upper())
 578 | 
 579 |             # let's try ipconfig under wine
 580 |             c = re.compile(
 581 |                 "\\s(" + "[0-9a-f]{2}-" * 5 + "[0-9a-f]{2})(\\s|$)",
 582 |                 re.IGNORECASE,
 583 |             )
 584 |             for line in os.popen("ipconfig /all"):
 585 |                 if m := c.search(line):
 586 |                     macaddrs.append(re.sub("-", ":", m[1]).upper())
 587 | 
 588 |         # extend the list of macaddrs in any case with the serials
 589 |         # cannot hurt ;-)
 590 |         macaddrs.extend(self._serials)
 591 | 
 592 |         return macaddrs
 593 | 
 594 |     def __getuserids(self):
 595 |         userids = []
 596 |         cursor = self.__cursor.execute("SELECT UserID FROM user")
 597 |         row = cursor.fetchone()
 598 |         while row is not None:
 599 |             with contextlib.suppress(Exception):
 600 |                 userid = row[0]
 601 |                 userids.append(userid)
 602 |             row = cursor.fetchone()
 603 |         return userids
 604 | 
 605 |     def __getuserkeys(self, macaddr):
 606 |         userids = self.__getuserids()
 607 |         userkeys = []
 608 |         for hash in KOBO_HASH_KEYS:
 609 |             deviceid = hashlib.sha256((hash + macaddr).encode("ascii")).hexdigest()
 610 |             for userid in userids:
 611 |                 userkey = hashlib.sha256(
 612 |                     (deviceid + userid).encode("ascii"),
 613 |                 ).hexdigest()
 614 |                 userkeys.append(binascii.a2b_hex(userkey[32:]))
 615 |         return userkeys
 616 | 
 617 | 
 618 | class KoboBook:
 619 |     """A Kobo book.
 620 | 
 621 |     A Kobo book contains a number of unencrypted and encrypted files.
 622 |     This class provides a list of the encrypted files.
 623 | 
 624 |     Each book has the following instance variables:
 625 |     volumeid - a UUID which uniquely refers to the book in this library.
 626 |     title - the human-readable book title.
 627 |     filename - the complete path and filename of the book.
 628 |     type - either kepub or drm-free"""
 629 | 
 630 |     def __init__(
 631 |         self,
 632 |         volumeid,
 633 |         title,
 634 |         filename,
 635 |         type,
 636 |         cursor,
 637 |         author=None,
 638 |         series=None,
 639 |     ) -> None:
 640 |         self.volumeid = volumeid
 641 |         self.title = title
 642 |         self.author = author
 643 |         self.series = series
 644 |         self.series_index = None
 645 |         self.filename = filename
 646 |         self.type = type
 647 |         self.__cursor = cursor
 648 |         self._encryptedfiles = {}
 649 | 
 650 |     @property
 651 |     def encryptedfiles(self):
 652 |         """A dictionary of KoboFiles inside the book.
 653 | 
 654 |         The dictionary keys are the relative pathnames, which are
 655 |         the same as the pathnames inside the book 'zip' file."""
 656 |         if self.type == "drm-free":
 657 |             return self._encryptedfiles
 658 |         if len(self._encryptedfiles) != 0:
 659 |             return self._encryptedfiles
 660 |         # Read the list of encrypted files from the DB
 661 |         for row in self.__cursor.execute(
 662 |             "SELECT elementid,elementkey FROM content_keys,content WHERE volumeid = ? AND volumeid = contentid",
 663 |             (self.volumeid,),
 664 |         ):
 665 |             self._encryptedfiles[row[0]] = KoboFile(
 666 |                 row[0],
 667 |                 None,
 668 |                 base64.b64decode(row[1]),
 669 |             )
 670 | 
 671 |         # Read the list of files from the kepub OPF manifest so that
 672 |         # we can get their proper MIME type.
 673 |         # NOTE: this requires that the OPF file is unencrypted!
 674 |         zin = zipfile.ZipFile(self.filename, "r")
 675 |         xmlns = {
 676 |             "ocf": "urn:oasis:names:tc:opendocument:xmlns:container",
 677 |             "opf": "http://www.idpf.org/2007/opf",
 678 |         }
 679 |         ocf = ET.fromstring(zin.read("META-INF/container.xml"))
 680 |         opffile = ocf.find(".//ocf:rootfile", xmlns).attrib["full-path"]
 681 |         basedir = re.sub("[^/]+$", "", opffile)
 682 |         opf = ET.fromstring(zin.read(opffile))
 683 |         zin.close()
 684 | 
 685 |         c = re.compile("/")
 686 |         for item in opf.findall(".//opf:item", xmlns):
 687 |             # Convert relative URIs
 688 |             href = item.attrib["href"]
 689 |             if not c.match(href):
 690 |                 href = "".join((basedir, href))
 691 | 
 692 |             # Update books we've found from the DB.
 693 |             if href in self._encryptedfiles:
 694 |                 mimetype = item.attrib["media-type"]
 695 |                 self._encryptedfiles[href].mimetype = mimetype
 696 |         return self._encryptedfiles
 697 | 
 698 |     @property
 699 |     def has_drm(self):
 700 |         return self.type != "drm-free"
 701 | 
 702 | 
 703 | class KoboFile:
 704 |     """An encrypted file in a KoboBook.
 705 | 
 706 |     Each file has the following instance variables:
 707 |     filename - the relative pathname inside the book zip file.
 708 |     mimetype - the file's MIME type, e.g. 'image/jpeg'
 709 |     key - the encrypted page key."""
 710 | 
 711 |     def __init__(self, filename, mimetype, key) -> None:
 712 |         self.filename = filename
 713 |         self.mimetype = mimetype
 714 |         self.key = key
 715 | 
 716 |     def decrypt(self, userkey, contents):
 717 |         """
 718 |         Decrypt the contents using the provided user key and the
 719 |         file page key. The caller must determine if the decrypted
 720 |         data is correct."""
 721 |         # The userkey decrypts the page key (self.key)
 722 |         keyenc = AES(userkey)
 723 |         decryptedkey = keyenc.decrypt(self.key)
 724 |         # The decrypted page key decrypts the content
 725 |         pageenc = AES(decryptedkey)
 726 |         return self.__removeaespadding(pageenc.decrypt(contents))
 727 | 
 728 |     def check(self, contents):
 729 |         """
 730 |         If the contents uses some known MIME types, check if it
 731 |         conforms to the type. Throw a ValueError exception if not.
 732 |         If the contents uses an uncheckable MIME type, don't check
 733 |         it and don't throw an exception.
 734 |         Returns True if the content was checked, False if it was not
 735 |         checked."""
 736 |         if self.mimetype == "application/xhtml+xml":
 737 |             # assume utf-8 with no BOM
 738 |             textoffset = 0
 739 |             stride = 1
 740 |             print(f"Checking text:{contents[:10]}:")
 741 |             # check for byte order mark
 742 |             if contents[:3] == b"\xef\xbb\xbf":
 743 |                 # seems to be utf-8 with BOM
 744 |                 print("Could be utf-8 with BOM")
 745 |                 textoffset = 3
 746 |             elif contents[:2] == b"\xfe\xff":
 747 |                 # seems to be utf-16BE
 748 |                 print("Could be  utf-16BE")
 749 |                 textoffset = 3
 750 |                 stride = 2
 751 |             elif contents[:2] == b"\xff\xfe":
 752 |                 # seems to be utf-16LE
 753 |                 print("Could be  utf-16LE")
 754 |                 textoffset = 2
 755 |                 stride = 2
 756 |             else:
 757 |                 print("Perhaps utf-8 without BOM")
 758 | 
 759 |             # now check that the first few characters are in the ASCII range
 760 |             for i in range(textoffset, textoffset + 5 * stride, stride):
 761 |                 if contents[i] < 32 or contents[i] > 127:
 762 |                     # Non-ascii, so decryption probably failed
 763 |                     print(f"Bad character at {i}, value {contents[i]}")
 764 |                     raise ValueError
 765 |             print("Seems to be good text")
 766 |             return True
 767 |         if self.mimetype == "image/jpeg":
 768 |             if contents[:3] == b"\xff\xd8\xff":
 769 |                 return True
 770 |             print(f"Bad JPEG: {contents[:3].hex()}")
 771 |             raise ValueError
 772 |         return False
 773 | 
 774 |     def __removeaespadding(self, contents):
 775 |         """
 776 |         Remove the trailing padding, using what appears to be the CMS
 777 |         algorithm from RFC 5652 6.3"""
 778 |         lastchar = binascii.b2a_hex(contents[-1:])
 779 |         strlen = int(lastchar, 16)
 780 |         padding = strlen
 781 |         if strlen == 1:
 782 |             return contents[:-1]
 783 |         if strlen < 16:
 784 |             for _ in range(strlen):
 785 |                 testchar = binascii.b2a_hex(contents[-strlen : -(strlen - 1)])
 786 |                 if testchar != lastchar:
 787 |                     padding = 0
 788 |         if padding > 0:
 789 |             contents = contents[:-padding]
 790 |         return contents
 791 | 
 792 | 
 793 | def decrypt_book(book, lib):
 794 |     print(f"Converting {book.title}")
 795 |     zin = zipfile.ZipFile(book.filename, "r")
 796 |     # make filename out of Unicode alphanumeric and whitespace equivalents from title
 797 |     outname = "{}.epub".format(re.sub("[^\\s\\w]", "_", book.title, 0, re.UNICODE))
 798 |     if book.type == "drm-free":
 799 |         print("DRM-free book, conversion is not needed")
 800 |         shutil.copyfile(book.filename, outname)
 801 |         print(f"Book saved as {os.path.join(os.getcwd(), outname)}")
 802 |         return os.path.join(os.getcwd(), outname)
 803 |     for userkey in lib.userkeys:
 804 |         print(f"Trying key: {userkey.hex()}")
 805 |         try:
 806 |             zout = zipfile.ZipFile(outname, "w", zipfile.ZIP_DEFLATED)
 807 |             for filename in zin.namelist():
 808 |                 contents = zin.read(filename)
 809 |                 if filename in book.encryptedfiles:
 810 |                     file = book.encryptedfiles[filename]
 811 |                     contents = file.decrypt(userkey, contents)
 812 |                     # Parse failures mean the key is probably wrong.
 813 |                     file.check(contents)
 814 |                 zout.writestr(filename, contents)
 815 |             zout.close()
 816 |             print("Decryption succeeded.")
 817 |             print(f"Book saved as {os.path.join(os.getcwd(), outname)}")
 818 |             break
 819 |         except ValueError:
 820 |             print("Decryption failed.")
 821 |             zout.close()
 822 |             os.remove(outname)
 823 |     zin.close()
 824 |     return os.path.join(os.getcwd(), outname)
 825 | 
 826 | 
 827 | def cli_main(devicedir):
 828 |     serials = []
 829 | 
 830 |     lib = KoboLibrary(serials, devicedir)
 831 | 
 832 |     for i, book in enumerate(lib.books):
 833 |         print(f"{i + 1}: {book.title}")
 834 | 
 835 |     choice = input("Convert book number... ")
 836 |     try:
 837 |         num = int(choice)
 838 |         books = [lib.books[num - 1]]
 839 |     except (ValueError, IndexError):
 840 |         print("Invalid choice. Exiting...")
 841 |         sys.exit()
 842 | 
 843 |     results = [decrypt_book(book, lib) for book in books]
 844 |     lib.close()
 845 |     return results[0]
 846 | 
 847 | 
 848 | if __name__ == "__main__":
 849 |     sys.stdout = SafeUnbuffered(sys.stdout)
 850 |     sys.stderr = SafeUnbuffered(sys.stderr)
 851 |     sys.exit(cli_main())

```

`/Users/arthrod/Library/CloudStorage/GoogleDrive-arthursrodrigues@gmail.com/My Drive/acode/atemp-drive/bilingual_book_maker/book_maker/translator/base_translator.py`:

```py
   1 | import itertools
   2 | from abc import ABC, abstractmethod
   3 | 
   4 | 
   5 | class Base(ABC):
   6 |     def __init__(self, key, language) -> None:
   7 |         self.keys = itertools.cycle(key.split(","))
   8 |         self.language = language
   9 | 
  10 |     @abstractmethod
  11 |     def rotate_key(self):
  12 |         pass
  13 | 
  14 |     @abstractmethod
  15 |     def translate(self, text):
  16 |         pass
  17 | 
  18 |     def set_deployment_id(self, deployment_id):
  19 |         pass

```

`/Users/arthrod/Library/CloudStorage/GoogleDrive-arthursrodrigues@gmail.com/My Drive/acode/atemp-drive/bilingual_book_maker/book_maker/translator/chatgptapi_translator.py`:

```py
   1 | import re
   2 | import time
   3 | import os
   4 | import shutil
   5 | from copy import copy
   6 | from os import environ
   7 | from itertools import cycle
   8 | import json
   9 | 
  10 | from openai import AzureOpenAI, OpenAI, RateLimitError
  11 | from rich import print
  12 | 
  13 | from .base_translator import Base
  14 | from ..config import config
  15 | 
  16 | CHATGPT_CONFIG = config["translator"]["chatgptapi"]
  17 | 
  18 | PROMPT_ENV_MAP = {
  19 |     "user": "BBM_CHATGPTAPI_USER_MSG_TEMPLATE",
  20 |     "system": "BBM_CHATGPTAPI_SYS_MSG",
  21 | }
  22 | 
  23 | GPT35_MODEL_LIST = [
  24 |     "gpt-3.5-turbo",
  25 |     "gpt-3.5-turbo-1106",
  26 |     "gpt-3.5-turbo-16k",
  27 |     "gpt-3.5-turbo-0613",
  28 |     "gpt-3.5-turbo-16k-0613",
  29 |     "gpt-3.5-turbo-0301",
  30 |     "gpt-3.5-turbo-0125",
  31 | ]
  32 | GPT4_MODEL_LIST = [
  33 |     "gpt-4-1106-preview",
  34 |     "gpt-4",
  35 |     "gpt-4-32k",
  36 |     "gpt-4o-2024-05-13",
  37 |     "gpt-4-0613",
  38 |     "gpt-4-32k-0613",
  39 | ]
  40 | 
  41 | GPT4oMINI_MODEL_LIST = [
  42 |     "gpt-4o-mini",
  43 |     "gpt-4o-mini-2024-07-18",
  44 | ]
  45 | GPT4o_MODEL_LIST = [
  46 |     "gpt-4o",
  47 |     "gpt-4o-2024-05-13",
  48 |     "gpt-4o-2024-08-06",
  49 |     "chatgpt-4o-latest",
  50 | ]
  51 | 
  52 | 
  53 | class ChatGPTAPI(Base):
  54 |     DEFAULT_PROMPT = "Please help me to translate,`{text}` to {language}, please return only translated content not include the origin text"
  55 | 
  56 |     def __init__(
  57 |         self,
  58 |         key,
  59 |         language,
  60 |         api_base=None,
  61 |         prompt_template=None,
  62 |         prompt_sys_msg=None,
  63 |         temperature=1.0,
  64 |         context_flag=False,
  65 |         context_paragraph_limit=0,
  66 |         **kwargs,
  67 |     ) -> None:
  68 |         super().__init__(key, language)
  69 |         self.key_len = len(key.split(","))
  70 |         self.openai_client = OpenAI(api_key=next(self.keys), base_url=api_base)
  71 |         self.api_base = api_base
  72 | 
  73 |         self.prompt_template = (
  74 |             prompt_template
  75 |             or environ.get(PROMPT_ENV_MAP["user"])
  76 |             or self.DEFAULT_PROMPT
  77 |         )
  78 |         self.prompt_sys_msg = (
  79 |             prompt_sys_msg
  80 |             or environ.get(
  81 |                 "OPENAI_API_SYS_MSG",
  82 |             )  # XXX: for backward compatibility, deprecate soon
  83 |             or environ.get(PROMPT_ENV_MAP["system"])
  84 |             or ""
  85 |         )
  86 |         self.system_content = environ.get("OPENAI_API_SYS_MSG") or ""
  87 |         self.deployment_id = None
  88 |         self.temperature = temperature
  89 |         self.model_list = None
  90 |         self.context_flag = context_flag
  91 |         self.context_list = []
  92 |         self.context_translated_list = []
  93 |         if context_paragraph_limit > 0:
  94 |             # not set by user, use default
  95 |             self.context_paragraph_limit = context_paragraph_limit
  96 |         else:
  97 |             # set by user, use user's value
  98 |             self.context_paragraph_limit = CHATGPT_CONFIG["context_paragraph_limit"]
  99 |         self.batch_text_list = []
 100 |         self.batch_info_cache = None
 101 |         self.result_content_cache = {}
 102 | 
 103 |     def rotate_key(self):
 104 |         self.openai_client.api_key = next(self.keys)
 105 | 
 106 |     def rotate_model(self):
 107 |         self.model = next(self.model_list)
 108 | 
 109 |     def create_messages(self, text, intermediate_messages=None):
 110 |         content = self.prompt_template.format(
 111 |             text=text, language=self.language, crlf="\n"
 112 |         )
 113 | 
 114 |         sys_content = self.system_content or self.prompt_sys_msg.format(crlf="\n")
 115 |         messages = [
 116 |             {"role": "system", "content": sys_content},
 117 |         ]
 118 | 
 119 |         if intermediate_messages:
 120 |             messages.extend(intermediate_messages)
 121 | 
 122 |         messages.append({"role": "user", "content": content})
 123 |         return messages
 124 | 
 125 |     def create_context_messages(self):
 126 |         messages = []
 127 |         if self.context_flag:
 128 |             messages.append({"role": "user", "content": "\n".join(self.context_list)})
 129 |             messages.append(
 130 |                 {
 131 |                     "role": "assistant",
 132 |                     "content": "\n".join(self.context_translated_list),
 133 |                 }
 134 |             )
 135 |         return messages
 136 | 
 137 |     def create_chat_completion(self, text):
 138 |         messages = self.create_messages(text, self.create_context_messages())
 139 |         completion = self.openai_client.chat.completions.create(
 140 |             model=self.model,
 141 |             messages=messages,
 142 |             temperature=self.temperature,
 143 |         )
 144 |         return completion
 145 | 
 146 |     def get_translation(self, text):
 147 |         self.rotate_key()
 148 |         self.rotate_model()  # rotate all the model to avoid the limit
 149 | 
 150 |         completion = self.create_chat_completion(text)
 151 | 
 152 |         # TODO work well or exception finish by length limit
 153 |         # Check if content is not None before encoding
 154 |         if completion.choices[0].message.content is not None:
 155 |             t_text = completion.choices[0].message.content.encode("utf8").decode() or ""
 156 |         else:
 157 |             t_text = ""
 158 | 
 159 |         if self.context_flag:
 160 |             self.save_context(text, t_text)
 161 | 
 162 |         return t_text
 163 | 
 164 |     def save_context(self, text, t_text):
 165 |         if self.context_paragraph_limit > 0:
 166 |             self.context_list.append(text)
 167 |             self.context_translated_list.append(t_text)
 168 |             # Remove the oldest context
 169 |             if len(self.context_list) > self.context_paragraph_limit:
 170 |                 self.context_list.pop(0)
 171 |                 self.context_translated_list.pop(0)
 172 | 
 173 |     def translate(self, text, needprint=True):
 174 |         start_time = time.time()
 175 |         # todo: Determine whether to print according to the cli option
 176 |         if needprint:
 177 |             print(re.sub("\n{3,}", "\n\n", text))
 178 | 
 179 |         attempt_count = 0
 180 |         max_attempts = 3
 181 |         t_text = ""
 182 | 
 183 |         while attempt_count < max_attempts:
 184 |             try:
 185 |                 t_text = self.get_translation(text)
 186 |                 break
 187 |             except RateLimitError as e:
 188 |                 # todo: better sleep time? why sleep alawys about key_len
 189 |                 # 1. openai server error or own network interruption, sleep for a fixed time
 190 |                 # 2. an apikey has no money or reach limit, don`t sleep, just replace it with another apikey
 191 |                 # 3. all apikey reach limit, then use current sleep
 192 |                 sleep_time = int(60 / self.key_len)
 193 |                 print(e, f"will sleep {sleep_time} seconds")
 194 |                 time.sleep(sleep_time)
 195 |                 attempt_count += 1
 196 |                 if attempt_count == max_attempts:
 197 |                     print(f"Get {attempt_count} consecutive exceptions")
 198 |                     raise
 199 |             except Exception as e:
 200 |                 print(str(e))
 201 |                 return
 202 | 
 203 |         # todo: Determine whether to print according to the cli option
 204 |         if needprint:
 205 |             print("[bold green]" + re.sub("\n{3,}", "\n\n", t_text) + "[/bold green]")
 206 | 
 207 |         time.time() - start_time
 208 |         # print(f"translation time: {elapsed_time:.1f}s")
 209 | 
 210 |         return t_text
 211 | 
 212 |     def translate_and_split_lines(self, text):
 213 |         result_str = self.translate(text, False)
 214 |         lines = result_str.splitlines()
 215 |         lines = [line.strip() for line in lines if line.strip() != ""]
 216 |         return lines
 217 | 
 218 |     def get_best_result_list(
 219 |         self,
 220 |         plist_len,
 221 |         new_str,
 222 |         sleep_dur,
 223 |         result_list,
 224 |         max_retries=15,
 225 |     ):
 226 |         if len(result_list) == plist_len:
 227 |             return result_list, 0
 228 | 
 229 |         best_result_list = result_list
 230 |         retry_count = 0
 231 | 
 232 |         while retry_count < max_retries and len(result_list) != plist_len:
 233 |             print(
 234 |                 f"bug: {plist_len} -> {len(result_list)} : Number of paragraphs before and after translation",
 235 |             )
 236 |             print(f"sleep for {sleep_dur}s and retry {retry_count+1} ...")
 237 |             time.sleep(sleep_dur)
 238 |             retry_count += 1
 239 |             result_list = self.translate_and_split_lines(new_str)
 240 |             if (
 241 |                 len(result_list) == plist_len
 242 |                 or len(best_result_list) < len(result_list) <= plist_len
 243 |                 or (
 244 |                     len(result_list) < len(best_result_list)
 245 |                     and len(best_result_list) > plist_len
 246 |                 )
 247 |             ):
 248 |                 best_result_list = result_list
 249 | 
 250 |         return best_result_list, retry_count
 251 | 
 252 |     def log_retry(self, state, retry_count, elapsed_time, log_path="log/buglog.txt"):
 253 |         if retry_count == 0:
 254 |             return
 255 |         print(f"retry {state}")
 256 |         with open(log_path, "a", encoding="utf-8") as f:
 257 |             print(
 258 |                 f"retry {state}, count = {retry_count}, time = {elapsed_time:.1f}s",
 259 |                 file=f,
 260 |             )
 261 | 
 262 |     def log_translation_mismatch(
 263 |         self,
 264 |         plist_len,
 265 |         result_list,
 266 |         new_str,
 267 |         sep,
 268 |         log_path="log/buglog.txt",
 269 |     ):
 270 |         if len(result_list) == plist_len:
 271 |             return
 272 |         newlist = new_str.split(sep)
 273 |         with open(log_path, "a", encoding="utf-8") as f:
 274 |             print(f"problem size: {plist_len - len(result_list)}", file=f)
 275 |             for i in range(len(newlist)):
 276 |                 print(newlist[i], file=f)
 277 |                 print(file=f)
 278 |                 if i < len(result_list):
 279 |                     print("............................................", file=f)
 280 |                     print(result_list[i], file=f)
 281 |                     print(file=f)
 282 |                 print("=============================", file=f)
 283 | 
 284 |         print(
 285 |             f"bug: {plist_len} paragraphs of text translated into {len(result_list)} paragraphs",
 286 |         )
 287 |         print("continue")
 288 | 
 289 |     def join_lines(self, text):
 290 |         lines = text.splitlines()
 291 |         new_lines = []
 292 |         temp_line = []
 293 | 
 294 |         # join
 295 |         for line in lines:
 296 |             if line.strip():
 297 |                 temp_line.append(line.strip())
 298 |             else:
 299 |                 if temp_line:
 300 |                     new_lines.append(" ".join(temp_line))
 301 |                     temp_line = []
 302 |                 new_lines.append(line)
 303 | 
 304 |         if temp_line:
 305 |             new_lines.append(" ".join(temp_line))
 306 | 
 307 |         text = "\n".join(new_lines)
 308 |         # try to fix #372
 309 |         if not text:
 310 |             return ""
 311 | 
 312 |         # del ^M
 313 |         text = text.replace("^M", "\r")
 314 |         lines = text.splitlines()
 315 |         filtered_lines = [line for line in lines if line.strip() != "\r"]
 316 |         new_text = "\n".join(filtered_lines)
 317 | 
 318 |         return new_text
 319 | 
 320 |     def translate_list(self, plist):
 321 |         sep = "\n\n\n\n\n"
 322 |         # new_str = sep.join([item.text for item in plist])
 323 | 
 324 |         new_str = ""
 325 |         i = 1
 326 |         for p in plist:
 327 |             temp_p = copy(p)
 328 |             for sup in temp_p.find_all("sup"):
 329 |                 sup.extract()
 330 |             new_str += f"({i}) {temp_p.get_text().strip()}{sep}"
 331 |             i = i + 1
 332 | 
 333 |         if new_str.endswith(sep):
 334 |             new_str = new_str[: -len(sep)]
 335 | 
 336 |         new_str = self.join_lines(new_str)
 337 | 
 338 |         plist_len = len(plist)
 339 | 
 340 |         print(f"plist len = {len(plist)}")
 341 | 
 342 |         result_list = self.translate_and_split_lines(new_str)
 343 | 
 344 |         start_time = time.time()
 345 | 
 346 |         result_list, retry_count = self.get_best_result_list(
 347 |             plist_len,
 348 |             new_str,
 349 |             6,  # WTF this magic number here?
 350 |             result_list,
 351 |         )
 352 | 
 353 |         end_time = time.time()
 354 | 
 355 |         state = "fail" if len(result_list) != plist_len else "success"
 356 |         log_path = "log/buglog.txt"
 357 | 
 358 |         self.log_retry(state, retry_count, end_time - start_time, log_path)
 359 |         self.log_translation_mismatch(plist_len, result_list, new_str, sep, log_path)
 360 | 
 361 |         # del (num), num. sometime (num) will translated to num.
 362 |         result_list = [re.sub(r"^(\(\d+\)|\d+\.|(\d+))\s*", "", s) for s in result_list]
 363 |         return result_list
 364 | 
 365 |     def set_deployment_id(self, deployment_id):
 366 |         self.deployment_id = deployment_id
 367 |         self.openai_client = AzureOpenAI(
 368 |             api_key=next(self.keys),
 369 |             azure_endpoint=self.api_base,
 370 |             api_version="2023-07-01-preview",
 371 |             azure_deployment=self.deployment_id,
 372 |         )
 373 | 
 374 |     def set_gpt35_models(self, ollama_model=""):
 375 |         if ollama_model:
 376 |             self.model_list = cycle([ollama_model])
 377 |             return
 378 |         # gpt3 all models for save the limit
 379 |         if self.deployment_id:
 380 |             self.model_list = cycle(["gpt-35-turbo"])
 381 |         else:
 382 |             my_model_list = [
 383 |                 i["id"] for i in self.openai_client.models.list().model_dump()["data"]
 384 |             ]
 385 |             model_list = list(set(my_model_list) & set(GPT35_MODEL_LIST))
 386 |             print(f"Using model list {model_list}")
 387 |             self.model_list = cycle(model_list)
 388 | 
 389 |     def set_gpt4_models(self):
 390 |         # for issue #375 azure can not use model list
 391 |         if self.deployment_id:
 392 |             self.model_list = cycle(["gpt-4"])
 393 |         else:
 394 |             my_model_list = [
 395 |                 i["id"] for i in self.openai_client.models.list().model_dump()["data"]
 396 |             ]
 397 |             model_list = list(set(my_model_list) & set(GPT4_MODEL_LIST))
 398 |             print(f"Using model list {model_list}")
 399 |             self.model_list = cycle(model_list)
 400 | 
 401 |     def set_gpt4omini_models(self):
 402 |         # for issue #375 azure can not use model list
 403 |         if self.deployment_id:
 404 |             self.model_list = cycle(["gpt-4o-mini"])
 405 |         else:
 406 |             my_model_list = [
 407 |                 i["id"] for i in self.openai_client.models.list().model_dump()["data"]
 408 |             ]
 409 |             model_list = list(set(my_model_list) & set(GPT4oMINI_MODEL_LIST))
 410 |             print(f"Using model list {model_list}")
 411 |             self.model_list = cycle(model_list)
 412 | 
 413 |     def set_gpt4o_models(self):
 414 |         # for issue #375 azure can not use model list
 415 |         if self.deployment_id:
 416 |             self.model_list = cycle(["gpt-4o"])
 417 |         else:
 418 |             my_model_list = [
 419 |                 i["id"] for i in self.openai_client.models.list().model_dump()["data"]
 420 |             ]
 421 |             model_list = list(set(my_model_list) & set(GPT4o_MODEL_LIST))
 422 |             print(f"Using model list {model_list}")
 423 |             self.model_list = cycle(model_list)
 424 | 
 425 |     def set_model_list(self, model_list):
 426 |         model_list = list(set(model_list))
 427 |         print(f"Using model list {model_list}")
 428 |         self.model_list = cycle(model_list)
 429 | 
 430 |     def batch_init(self, book_name):
 431 |         self.book_name = self.sanitize_book_name(book_name)
 432 | 
 433 |     def add_to_batch_translate_queue(self, book_index, text):
 434 |         self.batch_text_list.append({"book_index": book_index, "text": text})
 435 | 
 436 |     def sanitize_book_name(self, book_name):
 437 |         # Replace any characters that are not alphanumeric, underscore, hyphen, or dot with an underscore
 438 |         sanitized_book_name = re.sub(r"[^\w\-_\.]", "_", book_name)
 439 |         # Remove leading and trailing underscores and dots
 440 |         sanitized_book_name = sanitized_book_name.strip("._")
 441 |         return sanitized_book_name
 442 | 
 443 |     def batch_metadata_file_path(self):
 444 |         return os.path.join(os.getcwd(), "batch_files", f"{self.book_name}_info.json")
 445 | 
 446 |     def batch_dir(self):
 447 |         return os.path.join(os.getcwd(), "batch_files", self.book_name)
 448 | 
 449 |     def custom_id(self, book_index):
 450 |         return f"{self.book_name}-{book_index}"
 451 | 
 452 |     def is_completed_batch(self):
 453 |         batch_metadata_file_path = self.batch_metadata_file_path()
 454 | 
 455 |         if not os.path.exists(batch_metadata_file_path):
 456 |             print("Batch result file does not exist")
 457 |             raise Exception("Batch result file does not exist")
 458 | 
 459 |         with open(batch_metadata_file_path, "r", encoding="utf-8") as f:
 460 |             batch_info = json.load(f)
 461 | 
 462 |         for batch_file in batch_info["batch_files"]:
 463 |             batch_status = self.check_batch_status(batch_file["batch_id"])
 464 |             if batch_status.status != "completed":
 465 |                 return False
 466 | 
 467 |         return True
 468 | 
 469 |     def batch_translate(self, book_index):
 470 |         if self.batch_info_cache is None:
 471 |             batch_metadata_file_path = self.batch_metadata_file_path()
 472 |             with open(batch_metadata_file_path, "r", encoding="utf-8") as f:
 473 |                 self.batch_info_cache = json.load(f)
 474 | 
 475 |         batch_info = self.batch_info_cache
 476 |         target_batch = None
 477 |         for batch in batch_info["batch_files"]:
 478 |             if batch["start_index"] <= book_index < batch["end_index"]:
 479 |                 target_batch = batch
 480 |                 break
 481 | 
 482 |         if not target_batch:
 483 |             raise ValueError(f"No batch found for book_index {book_index}")
 484 | 
 485 |         if target_batch["batch_id"] in self.result_content_cache:
 486 |             result_content = self.result_content_cache[target_batch["batch_id"]]
 487 |         else:
 488 |             batch_status = self.check_batch_status(target_batch["batch_id"])
 489 |             if batch_status.output_file_id is None:
 490 |                 raise ValueError(f"Batch {target_batch['batch_id']} is not completed")
 491 |             result_content = self.get_batch_result(batch_status.output_file_id)
 492 |             self.result_content_cache[target_batch["batch_id"]] = result_content
 493 | 
 494 |         result_lines = result_content.text.split("\n")
 495 |         custom_id = self.custom_id(book_index)
 496 |         for line in result_lines:
 497 |             if line.strip():
 498 |                 result = json.loads(line)
 499 |                 if result["custom_id"] == custom_id:
 500 |                     return result["response"]["body"]["choices"][0]["message"][
 501 |                         "content"
 502 |                     ]
 503 | 
 504 |         raise ValueError(f"No result found for custom_id {custom_id}")
 505 | 
 506 |     def create_batch_context_messages(self, index):
 507 |         messages = []
 508 |         if self.context_flag:
 509 |             if index % CHATGPT_CONFIG[
 510 |                 "batch_context_update_interval"
 511 |             ] == 0 or not hasattr(self, "cached_context_messages"):
 512 |                 context_messages = []
 513 |                 for i in range(index - 1, -1, -1):
 514 |                     item = self.batch_text_list[i]
 515 |                     if len(item["text"].split()) >= 100:
 516 |                         context_messages.append(item["text"])
 517 |                         if len(context_messages) == self.context_paragraph_limit:
 518 |                             break
 519 | 
 520 |                 if len(context_messages) == self.context_paragraph_limit:
 521 |                     print("Creating cached context messages")
 522 |                     self.cached_context_messages = [
 523 |                         {"role": "user", "content": "\n".join(context_messages)},
 524 |                         {
 525 |                             "role": "assistant",
 526 |                             "content": self.get_translation(
 527 |                                 "\n".join(context_messages)
 528 |                             ),
 529 |                         },
 530 |                     ]
 531 | 
 532 |             if hasattr(self, "cached_context_messages"):
 533 |                 messages.extend(self.cached_context_messages)
 534 | 
 535 |         return messages
 536 | 
 537 |     def make_batch_request(self, book_index, text):
 538 |         messages = self.create_messages(
 539 |             text, self.create_batch_context_messages(book_index)
 540 |         )
 541 |         return {
 542 |             "custom_id": self.custom_id(book_index),
 543 |             "method": "POST",
 544 |             "url": "/v1/chat/completions",
 545 |             "body": {
 546 |                 # model shuould not be rotate
 547 |                 "model": self.batch_model,
 548 |                 "messages": messages,
 549 |                 "temperature": self.temperature,
 550 |             },
 551 |         }
 552 | 
 553 |     def create_batch_files(self, dest_file_path):
 554 |         file_paths = []
 555 |         # max request 50,000 and max size 100MB
 556 |         lines_per_file = 40000
 557 |         current_file = 0
 558 | 
 559 |         for i in range(0, len(self.batch_text_list), lines_per_file):
 560 |             current_file += 1
 561 |             file_path = os.path.join(dest_file_path, f"{current_file}.jsonl")
 562 |             start_index = i
 563 |             end_index = i + lines_per_file
 564 | 
 565 |             # TODO: Split the file if it exceeds 100MB
 566 |             with open(file_path, "w", encoding="utf-8") as f:
 567 |                 for text in self.batch_text_list[i : i + lines_per_file]:
 568 |                     batch_req = self.make_batch_request(
 569 |                         text["book_index"], text["text"]
 570 |                     )
 571 |                     json.dump(batch_req, f, ensure_ascii=False)
 572 |                     f.write("\n")
 573 |             file_paths.append(
 574 |                 {
 575 |                     "file_path": file_path,
 576 |                     "start_index": start_index,
 577 |                     "end_index": end_index,
 578 |                 }
 579 |             )
 580 | 
 581 |         return file_paths
 582 | 
 583 |     def batch(self):
 584 |         self.rotate_model()
 585 |         self.batch_model = self.model
 586 |         # current working directory
 587 |         batch_dir = self.batch_dir()
 588 |         batch_metadata_file_path = self.batch_metadata_file_path()
 589 |         # cleanup batch dir and result file
 590 |         if os.path.exists(batch_dir):
 591 |             shutil.rmtree(batch_dir)
 592 |         if os.path.exists(batch_metadata_file_path):
 593 |             os.remove(batch_metadata_file_path)
 594 |         os.makedirs(batch_dir, exist_ok=True)
 595 |         # batch execute
 596 |         batch_files = self.create_batch_files(batch_dir)
 597 |         batch_info = []
 598 |         for batch_file in batch_files:
 599 |             file_id = self.upload_batch_file(batch_file["file_path"])
 600 |             batch = self.batch_execute(file_id)
 601 |             batch_info.append(
 602 |                 self.create_batch_info(
 603 |                     file_id, batch, batch_file["start_index"], batch_file["end_index"]
 604 |                 )
 605 |             )
 606 |         # save batch info
 607 |         batch_info_json = {
 608 |             "book_id": self.book_name,
 609 |             "batch_date": time.strftime("%Y-%m-%d %H:%M:%S"),
 610 |             "batch_files": batch_info,
 611 |         }
 612 |         with open(batch_metadata_file_path, "w", encoding="utf-8") as f:
 613 |             json.dump(batch_info_json, f, ensure_ascii=False, indent=2)
 614 | 
 615 |     def create_batch_info(self, file_id, batch, start_index, end_index):
 616 |         return {
 617 |             "input_file_id": file_id,
 618 |             "batch_id": batch.id,
 619 |             "start_index": start_index,
 620 |             "end_index": end_index,
 621 |             "prefix": self.book_name,
 622 |         }
 623 | 
 624 |     def upload_batch_file(self, file_path):
 625 |         batch_input_file = self.openai_client.files.create(
 626 |             file=open(file_path, "rb"), purpose="batch"
 627 |         )
 628 |         return batch_input_file.id
 629 | 
 630 |     def batch_execute(self, file_id):
 631 |         current_time = time.strftime("%Y-%m-%d %H:%M:%S")
 632 |         res = self.openai_client.batches.create(
 633 |             input_file_id=file_id,
 634 |             endpoint="/v1/chat/completions",
 635 |             completion_window="24h",
 636 |             metadata={
 637 |                 "description": f"Batch job for {self.book_name} at {current_time}"
 638 |             },
 639 |         )
 640 |         if res.errors:
 641 |             print(res.errors)
 642 |             raise Exception(f"Batch execution failed: {res.errors}")
 643 |         return res
 644 | 
 645 |     def check_batch_status(self, batch_id):
 646 |         return self.openai_client.batches.retrieve(batch_id)
 647 | 
 648 |     def get_batch_result(self, output_file_id):
 649 |         return self.openai_client.files.content(output_file_id)

```

`/Users/arthrod/Library/CloudStorage/GoogleDrive-arthursrodrigues@gmail.com/My Drive/acode/atemp-drive/bilingual_book_maker/book_maker/translator/google_translator.py`:

```py
   1 | import re
   2 | import requests
   3 | from rich import print
   4 | 
   5 | 
   6 | from .base_translator import Base
   7 | 
   8 | 
   9 | class Google(Base):
  10 |     """
  11 |     google translate
  12 |     """
  13 | 
  14 |     def __init__(self, key, language, **kwargs) -> None:
  15 |         super().__init__(key, language)
  16 |         self.api_url = "https://translate.google.com/translate_a/single?client=it&dt=qca&dt=t&dt=rmt&dt=bd&dt=rms&dt=sos&dt=md&dt=gt&dt=ld&dt=ss&dt=ex&otf=2&dj=1&hl=en&ie=UTF-8&oe=UTF-8&sl=auto&tl=zh-CN"
  17 |         self.headers = {
  18 |             "Content-Type": "application/x-www-form-urlencoded",
  19 |             "User-Agent": "GoogleTranslate/6.29.59279 (iPhone; iOS 15.4; en; iPhone14,2)",
  20 |         }
  21 |         # TODO support more models here
  22 |         self.session = requests.session()
  23 |         self.language = language
  24 | 
  25 |     def rotate_key(self):
  26 |         pass
  27 | 
  28 |     def translate(self, text):
  29 |         print(text)
  30 |         """r = self.session.post(
  31 |             self.api_url,
  32 |             headers=self.headers,
  33 |             data=f"q={requests.utils.quote(text)}",
  34 |         )
  35 |         if not r.ok:
  36 |             return text
  37 |         t_text = "".join(
  38 |             [sentence.get("trans", "") for sentence in r.json()["sentences"]],
  39 |         )"""
  40 |         t_text = self._retry_translate(text)
  41 |         print("[bold green]" + re.sub("\n{3,}", "\n\n", t_text) + "[/bold green]")
  42 |         return t_text
  43 | 
  44 |     def _retry_translate(self, text, timeout=3):
  45 |         time = 0
  46 |         while time <= timeout:
  47 |             time += 1
  48 |             r = self.session.post(
  49 |                 self.api_url,
  50 |                 headers=self.headers,
  51 |                 data=f"q={requests.utils.quote(text)}",
  52 |                 timeout=3,
  53 |             )
  54 |             if r.ok:
  55 |                 t_text = "".join(
  56 |                     [sentence.get("trans", "") for sentence in r.json()["sentences"]],
  57 |                 )
  58 |                 return t_text
  59 |         return text

```

`/Users/arthrod/Library/CloudStorage/GoogleDrive-arthursrodrigues@gmail.com/My Drive/acode/atemp-drive/bilingual_book_maker/book_maker/translator/deepl_free_translator.py`:

```py
   1 | import time
   2 | import random
   3 | import re
   4 | 
   5 | from book_maker.utils import LANGUAGES, TO_LANGUAGE_CODE
   6 | 
   7 | from .base_translator import Base
   8 | from rich import print
   9 | from PyDeepLX import PyDeepLX
  10 | 
  11 | 
  12 | class DeepLFree(Base):
  13 |     """
  14 |     DeepL free translator
  15 |     """
  16 | 
  17 |     def __init__(self, key, language, **kwargs) -> None:
  18 |         super().__init__(key, language)
  19 |         l = None
  20 |         l = language if language in LANGUAGES else TO_LANGUAGE_CODE.get(language)
  21 |         if l not in [
  22 |             "bg",
  23 |             "zh",
  24 |             "cs",
  25 |             "da",
  26 |             "nl",
  27 |             "en-US",
  28 |             "en-GB",
  29 |             "et",
  30 |             "fi",
  31 |             "fr",
  32 |             "de",
  33 |             "el",
  34 |             "hu",
  35 |             "id",
  36 |             "it",
  37 |             "ja",
  38 |             "lv",
  39 |             "lt",
  40 |             "pl",
  41 |             "pt-PT",
  42 |             "pt-BR",
  43 |             "ro",
  44 |             "ru",
  45 |             "sk",
  46 |             "sl",
  47 |             "es",
  48 |             "sv",
  49 |             "tr",
  50 |             "uk",
  51 |             "ko",
  52 |             "nb",
  53 |         ]:
  54 |             raise Exception(f"DeepL do not support {l}")
  55 |         self.language = l
  56 |         self.time_random = [0.3, 0.5, 1, 1.3, 1.5, 2]
  57 | 
  58 |     def rotate_key(self):
  59 |         pass
  60 | 
  61 |     def translate(self, text):
  62 |         print(text)
  63 |         t_text = str(PyDeepLX.translate(text, "EN", self.language))
  64 |         # spider rule
  65 |         time.sleep(random.choice(self.time_random))
  66 |         print("[bold green]" + re.sub("\n{3,}", "\n\n", t_text) + "[/bold green]")
  67 |         return t_text

```

`/Users/arthrod/Library/CloudStorage/GoogleDrive-arthursrodrigues@gmail.com/My Drive/acode/atemp-drive/bilingual_book_maker/book_maker/translator/caiyun_translator.py`:

```py
   1 | import json
   2 | import re
   3 | import time
   4 | 
   5 | import requests
   6 | from rich import print
   7 | 
   8 | from .base_translator import Base
   9 | 
  10 | 
  11 | class Caiyun(Base):
  12 |     """
  13 |     caiyun translator
  14 |     """
  15 | 
  16 |     def __init__(self, key, language, **kwargs) -> None:
  17 |         super().__init__(key, language)
  18 |         self.api_url = "https://api.interpreter.caiyunai.com/v1/translator"
  19 |         self.headers = {
  20 |             "content-type": "application/json",
  21 |             "x-authorization": f"token {key}",
  22 |         }
  23 |         # caiyun api only supports: zh2en, zh2ja, en2zh, ja2zh
  24 |         self.translate_type = "auto2zh"
  25 |         if self.language == "english":
  26 |             self.translate_type = "auto2en"
  27 |         elif self.language == "japanese":
  28 |             self.translate_type = "auto2ja"
  29 | 
  30 |     def rotate_key(self):
  31 |         pass
  32 | 
  33 |     def translate(self, text):
  34 |         print(text)
  35 |         # for caiyun translate src issue #279
  36 |         text_list = text.splitlines()
  37 |         num = None
  38 |         if len(text_list) > 1:
  39 |             if text_list[0].isdigit():
  40 |                 num = text_list[0]
  41 |         payload = {
  42 |             "source": text,
  43 |             "trans_type": self.translate_type,
  44 |             "request_id": "demo",
  45 |             "detect": True,
  46 |         }
  47 |         response = requests.request(
  48 |             "POST",
  49 |             self.api_url,
  50 |             data=json.dumps(payload),
  51 |             headers=self.headers,
  52 |         )
  53 |         try:
  54 |             t_text = response.json()["target"]
  55 |         except Exception as e:
  56 |             print(str(e), response.text, "will sleep 60s for the time limit")
  57 |             if "limit" in response.json()["message"]:
  58 |                 print("will sleep 60s for the time limit")
  59 |             time.sleep(60)
  60 |             response = requests.request(
  61 |                 "POST",
  62 |                 self.api_url,
  63 |                 data=json.dumps(payload),
  64 |                 headers=self.headers,
  65 |             )
  66 |             t_text = response.json()["target"]
  67 | 
  68 |         print("[bold green]" + re.sub("\n{3,}", "\n\n", t_text) + "[/bold green]")
  69 |         # for issue #279
  70 |         if num:
  71 |             t_text = str(num) + "\n" + t_text
  72 |         return t_text

```

`/Users/arthrod/Library/CloudStorage/GoogleDrive-arthursrodrigues@gmail.com/My Drive/acode/atemp-drive/bilingual_book_maker/book_maker/translator/groq_translator.py`:

```py
   1 | from groq import Groq
   2 | from .chatgptapi_translator import ChatGPTAPI
   3 | from os import linesep
   4 | from itertools import cycle
   5 | 
   6 | 
   7 | GROQ_MODEL_LIST = [
   8 |     "llama3-8b-8192",
   9 |     "llama3-70b-8192",
  10 |     "mixtral-8x7b-32768",
  11 |     "gemma-7b-it",
  12 | ]
  13 | 
  14 | 
  15 | class GroqClient(ChatGPTAPI):
  16 |     def rotate_model(self):
  17 |         if not self.model_list:
  18 |             model_list = list(set(GROQ_MODEL_LIST))
  19 |             print(f"Using model list {model_list}")
  20 |             self.model_list = cycle(model_list)
  21 |         self.model = next(self.model_list)
  22 | 
  23 |     def create_chat_completion(self, text):
  24 |         self.groq_client = Groq(api_key=next(self.keys))
  25 | 
  26 |         content = f"{self.prompt_template.format(text=text, language=self.language, crlf=linesep)}"
  27 |         sys_content = self.system_content or self.prompt_sys_msg.format(crlf="\n")
  28 | 
  29 |         messages = [
  30 |             {"role": "system", "content": sys_content},
  31 |             {"role": "user", "content": content},
  32 |         ]
  33 | 
  34 |         if self.deployment_id:
  35 |             return self.groq_client.chat.completions.create(
  36 |                 engine=self.deployment_id,
  37 |                 messages=messages,
  38 |                 temperature=self.temperature,
  39 |                 azure=True,
  40 |             )
  41 |         return self.groq_client.chat.completions.create(
  42 |             model=self.model,
  43 |             messages=messages,
  44 |             temperature=self.temperature,
  45 |         )

```

`/Users/arthrod/Library/CloudStorage/GoogleDrive-arthursrodrigues@gmail.com/My Drive/acode/atemp-drive/bilingual_book_maker/book_maker/translator/__init__.py`:

```py
   1 | from book_maker.translator.caiyun_translator import Caiyun
   2 | from book_maker.translator.chatgptapi_translator import ChatGPTAPI
   3 | from book_maker.translator.deepl_translator import DeepL
   4 | from book_maker.translator.deepl_free_translator import DeepLFree
   5 | from book_maker.translator.google_translator import Google
   6 | from book_maker.translator.claude_translator import Claude
   7 | from book_maker.translator.gemini_translator import Gemini
   8 | from book_maker.translator.groq_translator import GroqClient
   9 | from book_maker.translator.tencent_transmart_translator import TencentTranSmart
  10 | from book_maker.translator.custom_api_translator import CustomAPI
  11 | from book_maker.translator.xai_translator import XAIClient
  12 | 
  13 | MODEL_DICT = {
  14 |     "openai": ChatGPTAPI,
  15 |     "chatgptapi": ChatGPTAPI,
  16 |     "gpt4": ChatGPTAPI,
  17 |     "gpt4omini": ChatGPTAPI,
  18 |     "gpt4o": ChatGPTAPI,
  19 |     "google": Google,
  20 |     "caiyun": Caiyun,
  21 |     "deepl": DeepL,
  22 |     "deeplfree": DeepLFree,
  23 |     "claude": Claude,
  24 |     "claude-3-5-sonnet-latest": Claude,
  25 |     "claude-3-5-sonnet-20241022": Claude,
  26 |     "claude-3-5-sonnet-20240620": Claude,
  27 |     "claude-3-5-haiku-latest": Claude,
  28 |     "claude-3-5-haiku-20241022": Claude,
  29 |     "gemini": Gemini,
  30 |     "geminipro": Gemini,
  31 |     "groq": GroqClient,
  32 |     "tencentransmart": TencentTranSmart,
  33 |     "customapi": CustomAPI,
  34 |     "xai": XAIClient,
  35 |     # add more here
  36 | }

```

`/Users/arthrod/Library/CloudStorage/GoogleDrive-arthursrodrigues@gmail.com/My Drive/acode/atemp-drive/bilingual_book_maker/book_maker/translator/custom_api_translator.py`:

```py
   1 | from .base_translator import Base
   2 | import re
   3 | import json
   4 | import requests
   5 | import time
   6 | from rich import print
   7 | 
   8 | 
   9 | class CustomAPI(Base):
  10 |     """
  11 |     Custom API translator
  12 |     """
  13 | 
  14 |     def __init__(self, custom_api, language, **kwargs) -> None:
  15 |         super().__init__(custom_api, language)
  16 |         self.language = language
  17 |         self.custom_api = custom_api
  18 | 
  19 |     def rotate_key(self):
  20 |         pass
  21 | 
  22 |     def translate(self, text):
  23 |         print(text)
  24 |         custom_api = self.custom_api
  25 |         data = {"text": text, "source_lang": "auto", "target_lang": self.language}
  26 |         post_data = json.dumps(data)
  27 |         r = requests.post(url=custom_api, data=post_data, timeout=10).text
  28 |         t_text = json.loads(r)["data"]
  29 |         print("[bold green]" + re.sub("\n{3,}", "\n\n", t_text) + "[/bold green]")
  30 |         time.sleep(5)
  31 |         return t_text

```

`/Users/arthrod/Library/CloudStorage/GoogleDrive-arthursrodrigues@gmail.com/My Drive/acode/atemp-drive/bilingual_book_maker/book_maker/translator/claude_translator.py`:

```py
   1 | import re
   2 | import time
   3 | from rich import print
   4 | from anthropic import Anthropic
   5 | 
   6 | from .base_translator import Base
   7 | 
   8 | 
   9 | class Claude(Base):
  10 |     def __init__(
  11 |         self,
  12 |         key,
  13 |         language,
  14 |         api_base=None,
  15 |         prompt_template=None,
  16 |         prompt_sys_msg=None,
  17 |         temperature=1.0,
  18 |         context_flag=False,
  19 |         context_paragraph_limit=5,
  20 |         **kwargs,
  21 |     ) -> None:
  22 |         super().__init__(key, language)
  23 |         self.api_url = api_base or "https://api.anthropic.com"
  24 |         self.client = Anthropic(base_url=api_base, api_key=key, timeout=20)
  25 |         self.model = "claude-3-5-sonnet-20241022"  # default it for now
  26 |         self.language = language
  27 |         self.prompt_template = (
  28 |             prompt_template
  29 |             or "Help me translate the text within triple backticks into {language} and provide only the translated result.\n```{text}```"
  30 |         )
  31 |         self.prompt_sys_msg = prompt_sys_msg or ""
  32 |         self.temperature = temperature
  33 |         self.context_flag = context_flag
  34 |         self.context_list = []
  35 |         self.context_translated_list = []
  36 |         self.context_paragraph_limit = context_paragraph_limit
  37 | 
  38 |     def rotate_key(self):
  39 |         pass
  40 | 
  41 |     def set_claude_model(self, model_name):
  42 |         self.model = model_name
  43 | 
  44 |     def create_messages(self, text, intermediate_messages=None):
  45 |         """Create messages for the current translation request"""
  46 |         current_msg = {
  47 |             "role": "user",
  48 |             "content": self.prompt_template.format(
  49 |                 text=text,
  50 |                 language=self.language,
  51 |             ),
  52 |         }
  53 | 
  54 |         messages = []
  55 |         if intermediate_messages:
  56 |             messages.extend(intermediate_messages)
  57 |         messages.append(current_msg)
  58 | 
  59 |         return messages
  60 | 
  61 |     def create_context_messages(self):
  62 |         """Create a message pair containing all context paragraphs"""
  63 |         if not self.context_flag or not self.context_list:
  64 |             return []
  65 | 
  66 |         # Create a single message pair for all previous context
  67 |         return [
  68 |             {
  69 |                 "role": "user",
  70 |                 "content": self.prompt_template.format(
  71 |                     text="\n\n".join(self.context_list),
  72 |                     language=self.language,
  73 |                 ),
  74 |             },
  75 |             {"role": "assistant", "content": "\n\n".join(self.context_translated_list)},
  76 |         ]
  77 | 
  78 |     def save_context(self, text, t_text):
  79 |         """Save the current translation pair to context"""
  80 |         if not self.context_flag:
  81 |             return
  82 | 
  83 |         self.context_list.append(text)
  84 |         self.context_translated_list.append(t_text)
  85 | 
  86 |         # Keep only the most recent paragraphs within the limit
  87 |         if len(self.context_list) > self.context_paragraph_limit:
  88 |             self.context_list.pop(0)
  89 |             self.context_translated_list.pop(0)
  90 | 
  91 |     def translate(self, text):
  92 |         print(text)
  93 |         self.rotate_key()
  94 | 
  95 |         # Create messages with context
  96 |         messages = self.create_messages(text, self.create_context_messages())
  97 | 
  98 |         r = self.client.messages.create(
  99 |             max_tokens=4096,
 100 |             messages=messages,
 101 |             system=self.prompt_sys_msg,
 102 |             temperature=self.temperature,
 103 |             model=self.model,
 104 |         )
 105 |         t_text = r.content[0].text
 106 | 
 107 |         if self.context_flag:
 108 |             self.save_context(text, t_text)
 109 | 
 110 |         print("[bold green]" + re.sub("\n{3,}", "\n\n", t_text) + "[/bold green]")
 111 |         return t_text

```

`/Users/arthrod/Library/CloudStorage/GoogleDrive-arthursrodrigues@gmail.com/My Drive/acode/atemp-drive/bilingual_book_maker/book_maker/translator/tencent_transmart_translator.py`:

```py
   1 | import re
   2 | import time
   3 | import uuid
   4 | import requests
   5 | 
   6 | from rich import print
   7 | from .base_translator import Base
   8 | 
   9 | 
  10 | class TencentTranSmart(Base):
  11 |     """
  12 |     Tencent TranSmart translator
  13 |     """
  14 | 
  15 |     def __init__(self, key, language, **kwargs) -> None:
  16 |         super().__init__(key, language)
  17 |         self.api_url = "https://transmart.qq.com/api/imt"
  18 |         self.header = {
  19 |             "authority": "transmart.qq.com",
  20 |             "content-type": "application/json",
  21 |             "origin": "https://transmart.qq.com",
  22 |             "referer": "https://transmart.qq.com/zh-CN/index",
  23 |             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
  24 |         }
  25 |         self.uuid = str(uuid.uuid4())
  26 |         self.session = requests.Session()
  27 |         self.translate_type = "zh"
  28 |         if self.language == "english":
  29 |             self.translate_type = "en"
  30 | 
  31 |     def rotate_key(self):
  32 |         pass
  33 | 
  34 |     def translate(self, text):
  35 |         print(text)
  36 |         source_language, text_list = self.text_analysis(text)
  37 |         client_key = self.get_client_key()
  38 |         api_form_data = {
  39 |             "header": {
  40 |                 "fn": "auto_translation",
  41 |                 "client_key": client_key,
  42 |             },
  43 |             "type": "plain",
  44 |             "model_category": "normal",
  45 |             "source": {
  46 |                 "lang": source_language,
  47 |                 "text_list": [""] + text_list + [""],
  48 |             },
  49 |             "target": {"lang": self.translate_type},
  50 |         }
  51 | 
  52 |         response = self.session.post(
  53 |             self.api_url, json=api_form_data, headers=self.header, timeout=3
  54 |         )
  55 |         t_text = "".join(response.json()["auto_translation"])
  56 |         print("[bold green]" + re.sub("\n{3,}", "\n\n", t_text) + "[/bold green]")
  57 |         return t_text
  58 | 
  59 |     def text_analysis(self, text):
  60 |         client_key = self.get_client_key()
  61 |         self.header.update({"Cookie": "TSMT_CLIENT_KEY={}".format(client_key)})
  62 |         analysis_request_data = {
  63 |             "header": {
  64 |                 "fn": "text_analysis",
  65 |                 "session": "",
  66 |                 "client_key": client_key,
  67 |                 "user": "",
  68 |             },
  69 |             "text": text,
  70 |             "type": "plain",
  71 |             "normalize": {"merge_broken_line": "false"},
  72 |         }
  73 |         r = self.session.post(
  74 |             self.api_url, json=analysis_request_data, headers=self.header
  75 |         )
  76 |         if not r.ok:
  77 |             return text
  78 |         response_json_data = r.json()
  79 |         text_list = [item["tgt_str"] for item in response_json_data["sentence_list"]]
  80 |         language = response_json_data["language"]
  81 |         return language, text_list
  82 | 
  83 |     def get_client_key(self):
  84 |         return "browser-chrome-121.0.0-Windows_10-{}-{}".format(
  85 |             self.uuid, int(time.time() * 1e3)
  86 |         )

```

`/Users/arthrod/Library/CloudStorage/GoogleDrive-arthursrodrigues@gmail.com/My Drive/acode/atemp-drive/bilingual_book_maker/book_maker/translator/deepl_translator.py`:

```py
   1 | import json
   2 | import time
   3 | 
   4 | import requests
   5 | import re
   6 | 
   7 | from book_maker.utils import LANGUAGES, TO_LANGUAGE_CODE
   8 | 
   9 | from .base_translator import Base
  10 | from rich import print
  11 | 
  12 | 
  13 | class DeepL(Base):
  14 |     """
  15 |     DeepL translator
  16 |     """
  17 | 
  18 |     def __init__(self, key, language, **kwargs) -> None:
  19 |         super().__init__(key, language)
  20 |         self.api_url = "https://dpl-translator.p.rapidapi.com/translate"
  21 |         self.headers = {
  22 |             "content-type": "application/json",
  23 |             "X-RapidAPI-Key": "",
  24 |             "X-RapidAPI-Host": "dpl-translator.p.rapidapi.com",
  25 |         }
  26 |         l = None
  27 |         l = language if language in LANGUAGES else TO_LANGUAGE_CODE.get(language)
  28 |         if l not in [
  29 |             "bg",
  30 |             "zh",
  31 |             "cs",
  32 |             "da",
  33 |             "nl",
  34 |             "en-US",
  35 |             "en-GB",
  36 |             "et",
  37 |             "fi",
  38 |             "fr",
  39 |             "de",
  40 |             "el",
  41 |             "hu",
  42 |             "id",
  43 |             "it",
  44 |             "ja",
  45 |             "lv",
  46 |             "lt",
  47 |             "pl",
  48 |             "pt-PT",
  49 |             "pt-BR",
  50 |             "ro",
  51 |             "ru",
  52 |             "sk",
  53 |             "sl",
  54 |             "es",
  55 |             "sv",
  56 |             "tr",
  57 |             "uk",
  58 |             "ko",
  59 |             "nb",
  60 |         ]:
  61 |             raise Exception(f"DeepL do not support {l}")
  62 |         self.language = l
  63 | 
  64 |     def rotate_key(self):
  65 |         self.headers["X-RapidAPI-Key"] = f"{next(self.keys)}"
  66 | 
  67 |     def translate(self, text):
  68 |         self.rotate_key()
  69 |         print(text)
  70 |         payload = {"text": text, "source": "EN", "target": self.language}
  71 |         try:
  72 |             response = requests.request(
  73 |                 "POST",
  74 |                 self.api_url,
  75 |                 data=json.dumps(payload),
  76 |                 headers=self.headers,
  77 |             )
  78 |         except Exception as e:
  79 |             print(e)
  80 |             time.sleep(30)
  81 |             response = requests.request(
  82 |                 "POST",
  83 |                 self.api_url,
  84 |                 data=json.dumps(payload),
  85 |                 headers=self.headers,
  86 |             )
  87 |         t_text = response.json().get("text", "")
  88 |         print("[bold green]" + re.sub("\n{3,}", "\n\n", t_text) + "[/bold green]")
  89 |         return t_text

```

`/Users/arthrod/Library/CloudStorage/GoogleDrive-arthursrodrigues@gmail.com/My Drive/acode/atemp-drive/bilingual_book_maker/book_maker/translator/xai_translator.py`:

```py
   1 | from openai import OpenAI
   2 | from .chatgptapi_translator import ChatGPTAPI
   3 | from os import linesep
   4 | from itertools import cycle
   5 | 
   6 | 
   7 | XAI_MODEL_LIST = [
   8 |     "grok-beta",
   9 | ]
  10 | 
  11 | 
  12 | class XAIClient(ChatGPTAPI):
  13 |     def __init__(self, key, language, api_base=None, **kwargs) -> None:
  14 |         super().__init__(key, language)
  15 |         self.model_list = XAI_MODEL_LIST
  16 |         self.api_url = str(api_base) if api_base else "https://api.x.ai/v1"
  17 |         self.openai_client = OpenAI(api_key=key, base_url=self.api_url)
  18 | 
  19 |     def rotate_model(self):
  20 |         self.model = self.model_list[0]

```

`/Users/arthrod/Library/CloudStorage/GoogleDrive-arthursrodrigues@gmail.com/My Drive/acode/atemp-drive/bilingual_book_maker/book_maker/translator/gemini_translator.py`:

```py
   1 | import re
   2 | import time
   3 | from os import environ
   4 | from itertools import cycle
   5 | 
   6 | import google.generativeai as genai
   7 | from google.generativeai.types.generation_types import (
   8 |     StopCandidateException,
   9 |     BlockedPromptException,
  10 | )
  11 | from rich import print
  12 | 
  13 | from .base_translator import Base
  14 | 
  15 | generation_config = {
  16 |     "temperature": 1.0,
  17 |     "top_p": 1,
  18 |     "top_k": 1,
  19 |     "max_output_tokens": 8192,
  20 | }
  21 | 
  22 | safety_settings = {
  23 |     "HATE": "BLOCK_NONE",
  24 |     "HARASSMENT": "BLOCK_NONE",
  25 |     "SEXUAL": "BLOCK_NONE",
  26 |     "DANGEROUS": "BLOCK_NONE",
  27 | }
  28 | 
  29 | PROMPT_ENV_MAP = {
  30 |     "user": "BBM_GEMINIAPI_USER_MSG_TEMPLATE",
  31 |     "system": "BBM_GEMINIAPI_SYS_MSG",
  32 | }
  33 | 
  34 | GEMINIPRO_MODEL_LIST = [
  35 |     "gemini-1.5-pro",
  36 |     "gemini-1.5-pro-latest",
  37 |     "gemini-1.5-pro-001",
  38 |     "gemini-1.5-pro-002",
  39 | ]
  40 | 
  41 | GEMINIFLASH_MODEL_LIST = [
  42 |     "gemini-1.5-flash",
  43 |     "gemini-1.5-flash-latest",
  44 |     "gemini-1.5-flash-001",
  45 |     "gemini-1.5-flash-002",
  46 |     "gemini-2.0-flash-exp",
  47 | ]
  48 | 
  49 | 
  50 | class Gemini(Base):
  51 |     """
  52 |     Google gemini translator
  53 |     """
  54 | 
  55 |     DEFAULT_PROMPT = "Please help me to translate,`{text}` to {language}, please return only translated content not include the origin text"
  56 | 
  57 |     def __init__(
  58 |         self,
  59 |         key,
  60 |         language,
  61 |         prompt_template=None,
  62 |         prompt_sys_msg=None,
  63 |         context_flag=False,
  64 |         temperature=1.0,
  65 |         **kwargs,
  66 |     ) -> None:
  67 |         super().__init__(key, language)
  68 |         self.context_flag = context_flag
  69 |         self.prompt = (
  70 |             prompt_template
  71 |             or environ.get(PROMPT_ENV_MAP["user"])
  72 |             or self.DEFAULT_PROMPT
  73 |         )
  74 |         self.prompt_sys_msg = (
  75 |             prompt_sys_msg
  76 |             or environ.get(PROMPT_ENV_MAP["system"])
  77 |             or None  # Allow None, but not empty string
  78 |         )
  79 |         self.interval = 3
  80 |         genai.configure(api_key=next(self.keys))
  81 |         generation_config["temperature"] = temperature
  82 | 
  83 |     def create_convo(self):
  84 |         model = genai.GenerativeModel(
  85 |             model_name=self.model,
  86 |             generation_config=generation_config,
  87 |             safety_settings=safety_settings,
  88 |             system_instruction=self.prompt_sys_msg,
  89 |         )
  90 |         self.convo = model.start_chat()
  91 |         # print(model)  # Uncomment to debug and inspect the model details.
  92 | 
  93 |     def rotate_model(self):
  94 |         self.model = next(self.model_list)
  95 |         self.create_convo()
  96 |         print(f"Using model {self.model}")
  97 | 
  98 |     def rotate_key(self):
  99 |         genai.configure(api_key=next(self.keys))
 100 |         self.create_convo()
 101 | 
 102 |     def translate(self, text):
 103 |         delay = 1
 104 |         exponential_base = 2
 105 |         attempt_count = 0
 106 |         max_attempts = 7
 107 | 
 108 |         t_text = ""
 109 |         print(text)
 110 |         # same for caiyun translate src issue #279 gemini for #374
 111 |         text_list = text.splitlines()
 112 |         num = None
 113 |         if len(text_list) > 1:
 114 |             if text_list[0].isdigit():
 115 |                 num = text_list[0]
 116 | 
 117 |         while attempt_count < max_attempts:
 118 |             try:
 119 |                 self.convo.send_message(
 120 |                     self.prompt.format(text=text, language=self.language)
 121 |                 )
 122 |                 t_text = self.convo.last.text.strip()
 123 |                 # 检查是否包含特定标签,如果有则只返回标签内的内容
 124 |                 tag_pattern = (
 125 |                     r"<step3_refined_translation>(.*?)</step3_refined_translation>"
 126 |                 )
 127 |                 tag_match = re.search(tag_pattern, t_text, re.DOTALL)
 128 |                 if tag_match:
 129 |                     print(
 130 |                         "[bold green]"
 131 |                         + re.sub("\n{3,}", "\n\n", t_text)
 132 |                         + "[/bold green]"
 133 |                     )
 134 |                     t_text = tag_match.group(1).strip()
 135 |                     # print("[bold green]" + re.sub("\n{3,}", "\n\n", t_text) + "[/bold green]")
 136 |                 break
 137 |             except StopCandidateException as e:
 138 |                 print(
 139 |                     f"Translation failed due to StopCandidateException: {e} Attempting to switch model..."
 140 |                 )
 141 |                 self.rotate_model()
 142 |             except BlockedPromptException as e:
 143 |                 print(
 144 |                     f"Translation failed due to BlockedPromptException: {e} Attempting to switch model..."
 145 |                 )
 146 |                 self.rotate_model()
 147 |             except Exception as e:
 148 |                 print(
 149 |                     f"Translation failed due to {type(e).__name__}: {e} Will sleep {delay} seconds"
 150 |                 )
 151 |                 time.sleep(delay)
 152 |                 delay *= exponential_base
 153 | 
 154 |                 self.rotate_key()
 155 |                 if attempt_count >= 1:
 156 |                     self.rotate_model()
 157 | 
 158 |             attempt_count += 1
 159 | 
 160 |         if attempt_count == max_attempts:
 161 |             print(f"Translation failed after {max_attempts} attempts.")
 162 |             return
 163 | 
 164 |         if self.context_flag:
 165 |             if len(self.convo.history) > 10:
 166 |                 self.convo.history = self.convo.history[2:]
 167 |         else:
 168 |             self.convo.history = []
 169 | 
 170 |         print("[bold green]" + re.sub("\n{3,}", "\n\n", t_text) + "[/bold green]")
 171 |         # for rate limit(RPM)
 172 |         time.sleep(self.interval)
 173 |         if num:
 174 |             t_text = str(num) + "\n" + t_text
 175 |         return t_text
 176 | 
 177 |     def set_interval(self, interval):
 178 |         self.interval = interval
 179 | 
 180 |     def set_geminipro_models(self):
 181 |         self.set_models(GEMINIPRO_MODEL_LIST)
 182 | 
 183 |     def set_geminiflash_models(self):
 184 |         self.set_models(GEMINIFLASH_MODEL_LIST)
 185 | 
 186 |     def set_models(self, allowed_models):
 187 |         available_models = [
 188 |             re.sub(r"^models/", "", i.name) for i in genai.list_models()
 189 |         ]
 190 |         model_list = sorted(
 191 |             list(set(available_models) & set(allowed_models)),
 192 |             key=allowed_models.index,
 193 |         )
 194 |         print(f"Using model list {model_list}")
 195 |         self.model_list = cycle(model_list)
 196 |         self.rotate_model()
 197 | 
 198 |     def set_model_list(self, model_list):
 199 |         # keep the order of input
 200 |         model_list = sorted(list(set(model_list)), key=model_list.index)
 201 |         print(f"Using model list {model_list}")
 202 |         self.model_list = cycle(model_list)
 203 |         self.rotate_model()

```

`/Users/arthrod/Library/CloudStorage/GoogleDrive-arthursrodrigues@gmail.com/My Drive/acode/atemp-drive/bilingual_book_maker/book_maker/translator/litellm_translator.py`:

```py
   1 | from os import linesep
   2 | 
   3 | from litellm import completion
   4 | 
   5 | from book_maker.translator.chatgptapi_translator import ChatGPTAPI
   6 | 
   7 | PROMPT_ENV_MAP = {
   8 |     "user": "BBM_CHATGPTAPI_USER_MSG_TEMPLATE",
   9 |     "system": "BBM_CHATGPTAPI_SYS_MSG",
  10 | }
  11 | 
  12 | 
  13 | class liteLLM(ChatGPTAPI):
  14 |     def create_chat_completion(self, text):
  15 |         # content = self.prompt_template.format(
  16 |         #     text=text, language=self.language, crlf="\n"
  17 |         # )
  18 | 
  19 |         content = f"{self.context if self.context_flag else ''} {self.prompt_template.format(text=text, language=self.language, crlf=linesep)}"
  20 | 
  21 |         sys_content = self.system_content or self.prompt_sys_msg.format(crlf="\n")
  22 | 
  23 |         context_sys_str = "For each passage given, you may be provided a summary of the story up until this point (wrapped in tags '<summary>' and '</summary>') for context within the query, to provide background context of the story up until this point. If it's provided, use the context summary to aid you in translation with deeper comprehension, and write a new summary above the returned translation, wrapped in '<summary>' HTML-like tags, including important details (if relevant) from the new passage, retaining the most important key details from the existing summary, and dropping out less important details. If the summary is blank, assume it is the start of the story and write a summary from scratch. Do not make the summary longer than a paragraph, and smaller details can be replaced based on the relative importance of new details. The summary should be formatted in straightforward, inornate text, briefly summarising the entire story (from the start, including information before the given passage, leading up to the given passage) to act as an instructional payload for a Large-Language AI Model to fully understand the context of the passage."
  24 | 
  25 |         sys_content = f"{self.system_content or self.prompt_sys_msg.format(crlf=linesep)} {context_sys_str if self.context_flag else ''} "
  26 | 
  27 |         messages = [
  28 |             {"role": "system", "content": sys_content},
  29 |             {"role": "user", "content": content},
  30 |         ]
  31 | 
  32 |         if self.deployment_id:
  33 |             return completion(
  34 |                 engine=self.deployment_id,
  35 |                 messages=messages,
  36 |                 temperature=self.temperature,
  37 |                 azure=True,
  38 |             )
  39 | 
  40 |         return completion(
  41 |             model="gpt-3.5-turbo",
  42 |             messages=messages,
  43 |             temperature=self.temperature,
  44 |         )

```

`/Users/arthrod/Library/CloudStorage/GoogleDrive-arthursrodrigues@gmail.com/My Drive/acode/atemp-drive/bilingual_book_maker/book_maker/cli.py`:

```py
   1 | import argparse
   2 | import json
   3 | import os
   4 | from os import environ as env
   5 | 
   6 | from book_maker.loader import BOOK_LOADER_DICT
   7 | from book_maker.translator import MODEL_DICT
   8 | from book_maker.utils import LANGUAGES, TO_LANGUAGE_CODE
   9 | 
  10 | 
  11 | def parse_prompt_arg(prompt_arg):
  12 |     prompt = None
  13 |     if prompt_arg is None:
  14 |         return prompt
  15 | 
  16 |     if not any(prompt_arg.endswith(ext) for ext in [".json", ".txt"]):
  17 |         try:
  18 |             # user can define prompt by passing a json string
  19 |             # eg: --prompt '{"system": "You are a professional translator who translates computer technology books", "user": "Translate \`{text}\` to {language}"}'
  20 |             prompt = json.loads(prompt_arg)
  21 |         except json.JSONDecodeError:
  22 |             # if not a json string, treat it as a template string
  23 |             prompt = {"user": prompt_arg}
  24 | 
  25 |     elif os.path.exists(prompt_arg):
  26 |         if prompt_arg.endswith(".txt"):
  27 |             # if it's a txt file, treat it as a template string
  28 |             with open(prompt_arg, encoding="utf-8") as f:
  29 |                 prompt = {"user": f.read()}
  30 |         elif prompt_arg.endswith(".json"):
  31 |             # if it's a json file, treat it as a json object
  32 |             # eg: --prompt prompt_template_sample.json
  33 |             with open(prompt_arg, encoding="utf-8") as f:
  34 |                 prompt = json.load(f)
  35 |     else:
  36 |         raise FileNotFoundError(f"{prompt_arg} not found")
  37 | 
  38 |     # if prompt is None or any(c not in prompt["user"] for c in ["{text}", "{language}"]):
  39 |     if prompt is None or any(c not in prompt["user"] for c in ["{text}"]):
  40 |         raise ValueError("prompt must contain `{text}`")
  41 | 
  42 |     if "user" not in prompt:
  43 |         raise ValueError("prompt must contain the key of `user`")
  44 | 
  45 |     if (prompt.keys() - {"user", "system"}) != set():
  46 |         raise ValueError("prompt can only contain the keys of `user` and `system`")
  47 | 
  48 |     print("prompt config:", prompt)
  49 |     return prompt
  50 | 
  51 | 
  52 | def main():
  53 |     translate_model_list = list(MODEL_DICT.keys())
  54 |     parser = argparse.ArgumentParser()
  55 |     parser.add_argument(
  56 |         "--book_name",
  57 |         dest="book_name",
  58 |         type=str,
  59 |         help="path of the epub file to be translated",
  60 |     )
  61 |     parser.add_argument(
  62 |         "--book_from",
  63 |         dest="book_from",
  64 |         type=str,
  65 |         choices=["kobo"],  # support kindle later
  66 |         metavar="E-READER",
  67 |         help="e-reader type, available: {%(choices)s}",
  68 |     )
  69 |     parser.add_argument(
  70 |         "--device_path",
  71 |         dest="device_path",
  72 |         type=str,
  73 |         help="Path of e-reader device",
  74 |     )
  75 |     ########## KEYS ##########
  76 |     parser.add_argument(
  77 |         "--openai_key",
  78 |         dest="openai_key",
  79 |         type=str,
  80 |         default="",
  81 |         help="OpenAI api key,if you have more than one key, please use comma"
  82 |         " to split them to go beyond the rate limits",
  83 |     )
  84 |     parser.add_argument(
  85 |         "--caiyun_key",
  86 |         dest="caiyun_key",
  87 |         type=str,
  88 |         help="you can apply caiyun key from here (https://dashboard.caiyunapp.com/user/sign_in/)",
  89 |     )
  90 |     parser.add_argument(
  91 |         "--deepl_key",
  92 |         dest="deepl_key",
  93 |         type=str,
  94 |         help="you can apply deepl key from here (https://rapidapi.com/splintPRO/api/dpl-translator",
  95 |     )
  96 |     parser.add_argument(
  97 |         "--claude_key",
  98 |         dest="claude_key",
  99 |         type=str,
 100 |         help="you can find claude key from here (https://console.anthropic.com/account/keys)",
 101 |     )
 102 | 
 103 |     parser.add_argument(
 104 |         "--custom_api",
 105 |         dest="custom_api",
 106 |         type=str,
 107 |         help="you should build your own translation api",
 108 |     )
 109 | 
 110 |     # for Google Gemini
 111 |     parser.add_argument(
 112 |         "--gemini_key",
 113 |         dest="gemini_key",
 114 |         type=str,
 115 |         help="You can get Gemini Key from  https://makersuite.google.com/app/apikey",
 116 |     )
 117 | 
 118 |     # for Groq
 119 |     parser.add_argument(
 120 |         "--groq_key",
 121 |         dest="groq_key",
 122 |         type=str,
 123 |         help="You can get Groq Key from  https://console.groq.com/keys",
 124 |     )
 125 | 
 126 |     # for xAI
 127 |     parser.add_argument(
 128 |         "--xai_key",
 129 |         dest="xai_key",
 130 |         type=str,
 131 |         help="You can get xAI Key from  https://console.x.ai/",
 132 |     )
 133 | 
 134 |     parser.add_argument(
 135 |         "--test",
 136 |         dest="test",
 137 |         action="store_true",
 138 |         help="only the first 10 paragraphs will be translated, for testing",
 139 |     )
 140 |     parser.add_argument(
 141 |         "--test_num",
 142 |         dest="test_num",
 143 |         type=int,
 144 |         default=10,
 145 |         help="how many paragraphs will be translated for testing",
 146 |     )
 147 |     parser.add_argument(
 148 |         "-m",
 149 |         "--model",
 150 |         dest="model",
 151 |         type=str,
 152 |         default="chatgptapi",
 153 |         choices=translate_model_list,  # support DeepL later
 154 |         metavar="MODEL",
 155 |         help="model to use, available: {%(choices)s}",
 156 |     )
 157 |     parser.add_argument(
 158 |         "--ollama_model",
 159 |         dest="ollama_model",
 160 |         type=str,
 161 |         default="",
 162 |         metavar="MODEL",
 163 |         help="use ollama",
 164 |     )
 165 |     parser.add_argument(
 166 |         "--language",
 167 |         type=str,
 168 |         choices=sorted(LANGUAGES.keys())
 169 |         + sorted([k.title() for k in TO_LANGUAGE_CODE]),
 170 |         default="zh-hans",
 171 |         metavar="LANGUAGE",
 172 |         help="language to translate to, available: {%(choices)s}",
 173 |     )
 174 |     parser.add_argument(
 175 |         "--resume",
 176 |         dest="resume",
 177 |         action="store_true",
 178 |         help="if program stop unexpected you can use this to resume",
 179 |     )
 180 |     parser.add_argument(
 181 |         "-p",
 182 |         "--proxy",
 183 |         dest="proxy",
 184 |         type=str,
 185 |         default="",
 186 |         help="use proxy like http://127.0.0.1:7890",
 187 |     )
 188 |     parser.add_argument(
 189 |         "--deployment_id",
 190 |         dest="deployment_id",
 191 |         type=str,
 192 |         help="the deployment name you chose when you deployed the model",
 193 |     )
 194 |     # args to change api_base
 195 |     parser.add_argument(
 196 |         "--api_base",
 197 |         metavar="API_BASE_URL",
 198 |         dest="api_base",
 199 |         type=str,
 200 |         help="specify base url other than the OpenAI's official API address",
 201 |     )
 202 |     parser.add_argument(
 203 |         "--exclude_filelist",
 204 |         dest="exclude_filelist",
 205 |         type=str,
 206 |         default="",
 207 |         help="if you have more than one file to exclude, please use comma to split them, example: --exclude_filelist 'nav.xhtml,cover.xhtml'",
 208 |     )
 209 |     parser.add_argument(
 210 |         "--only_filelist",
 211 |         dest="only_filelist",
 212 |         type=str,
 213 |         default="",
 214 |         help="if you only have a few files with translations, please use comma to split them, example: --only_filelist 'nav.xhtml,cover.xhtml'",
 215 |     )
 216 |     parser.add_argument(
 217 |         "--translate-tags",
 218 |         dest="translate_tags",
 219 |         type=str,
 220 |         default="p",
 221 |         help="example --translate-tags p,blockquote",
 222 |     )
 223 |     parser.add_argument(
 224 |         "--exclude_translate-tags",
 225 |         dest="exclude_translate_tags",
 226 |         type=str,
 227 |         default="sup",
 228 |         help="example --exclude_translate-tags table,sup",
 229 |     )
 230 |     parser.add_argument(
 231 |         "--allow_navigable_strings",
 232 |         dest="allow_navigable_strings",
 233 |         action="store_true",
 234 |         default=False,
 235 |         help="allow NavigableStrings to be translated",
 236 |     )
 237 |     parser.add_argument(
 238 |         "--prompt",
 239 |         dest="prompt_arg",
 240 |         type=str,
 241 |         metavar="PROMPT_ARG",
 242 |         help="used for customizing the prompt. It can be the prompt template string, or a path to the template file. The valid placeholders are `{text}` and `{language}`.",
 243 |     )
 244 |     parser.add_argument(
 245 |         "--accumulated_num",
 246 |         dest="accumulated_num",
 247 |         type=int,
 248 |         default=1,
 249 |         help="""Wait for how many tokens have been accumulated before starting the translation.
 250 | gpt3.5 limits the total_token to 4090.
 251 | For example, if you use --accumulated_num 1600, maybe openai will output 2200 tokens
 252 | and maybe 200 tokens for other messages in the system messages user messages, 1600+2200+200=4000,
 253 | So you are close to reaching the limit. You have to choose your own value, there is no way to know if the limit is reached before sending
 254 | """,
 255 |     )
 256 |     parser.add_argument(
 257 |         "--translation_style",
 258 |         dest="translation_style",
 259 |         type=str,
 260 |         help="""ex: --translation_style "color: #808080; font-style: italic;" """,
 261 |     )
 262 |     parser.add_argument(
 263 |         "--batch_size",
 264 |         dest="batch_size",
 265 |         type=int,
 266 |         help="how many lines will be translated by aggregated translation(This options currently only applies to txt files)",
 267 |     )
 268 |     parser.add_argument(
 269 |         "--retranslate",
 270 |         dest="retranslate",
 271 |         nargs=4,
 272 |         type=str,
 273 |         help="""--retranslate "$translated_filepath" "file_name_in_epub" "start_str" "end_str"(optional)
 274 |         Retranslate from start_str to end_str's tag:
 275 |         python3 "make_book.py" --book_name "test_books/animal_farm.epub" --retranslate 'test_books/animal_farm_bilingual.epub' 'index_split_002.html' 'in spite of the present book shortage which' 'This kind of thing is not a good symptom. Obviously'
 276 |         Retranslate start_str's tag:
 277 |         python3 "make_book.py" --book_name "test_books/animal_farm.epub" --retranslate 'test_books/animal_farm_bilingual.epub' 'index_split_002.html' 'in spite of the present book shortage which'
 278 | """,
 279 |     )
 280 |     parser.add_argument(
 281 |         "--single_translate",
 282 |         action="store_true",
 283 |         help="output translated book, no bilingual",
 284 |     )
 285 |     parser.add_argument(
 286 |         "--use_context",
 287 |         dest="context_flag",
 288 |         action="store_true",
 289 |         help="adds an additional paragraph for global, updating historical context of the story to the model's input, improving the narrative consistency for the AI model (this uses ~200 more tokens each time)",
 290 |     )
 291 |     parser.add_argument(
 292 |         "--context_paragraph_limit",
 293 |         dest="context_paragraph_limit",
 294 |         type=int,
 295 |         default=0,
 296 |         help="if use --use_context, set context paragraph limit",
 297 |     )
 298 |     parser.add_argument(
 299 |         "--temperature",
 300 |         type=float,
 301 |         default=1.0,
 302 |         help="temperature parameter for `chatgptapi`/`gpt4`/`claude`/`gemini`",
 303 |     )
 304 |     parser.add_argument(
 305 |         "--block_size",
 306 |         type=int,
 307 |         default=-1,
 308 |         help="merge multiple paragraphs into one block, may increase accuracy and speed up the process, but disturb the original format, must be used with `--single_translate`",
 309 |     )
 310 |     parser.add_argument(
 311 |         "--model_list",
 312 |         type=str,
 313 |         dest="model_list",
 314 |         help="Rather than using our preset lists of models, specify exactly the models you want as a comma separated list `gpt-4-32k,gpt-3.5-turbo-0125` (Currently only supports: `openai`)",
 315 |     )
 316 |     parser.add_argument(
 317 |         "--batch",
 318 |         dest="batch_flag",
 319 |         action="store_true",
 320 |         help="Enable batch translation using ChatGPT's batch API for improved efficiency",
 321 |     )
 322 |     parser.add_argument(
 323 |         "--batch-use",
 324 |         dest="batch_use_flag",
 325 |         action="store_true",
 326 |         help="Use pre-generated batch translations to create files. Run with --batch first before using this option",
 327 |     )
 328 |     parser.add_argument(
 329 |         "--interval",
 330 |         type=float,
 331 |         default=0.01,
 332 |         help="Request interval in seconds (e.g., 0.1 for 100ms). Currently only supported for Gemini models. Default: 0.01",
 333 |     )
 334 | 
 335 |     options = parser.parse_args()
 336 | 
 337 |     if not options.book_name:
 338 |         print(f"Error: please provide the path of your book using --book_name <path>")
 339 |         exit(1)
 340 |     if not os.path.isfile(options.book_name):
 341 |         print(f"Error: the book {options.book_name!r} does not exist.")
 342 |         exit(1)
 343 | 
 344 |     PROXY = options.proxy
 345 |     if PROXY != "":
 346 |         os.environ["http_proxy"] = PROXY
 347 |         os.environ["https_proxy"] = PROXY
 348 | 
 349 |     translate_model = MODEL_DICT.get(options.model)
 350 |     assert translate_model is not None, "unsupported model"
 351 |     API_KEY = ""
 352 |     if options.model in ["openai", "chatgptapi", "gpt4", "gpt4omini", "gpt4o"]:
 353 |         if OPENAI_API_KEY := (
 354 |             options.openai_key
 355 |             or env.get(
 356 |                 "OPENAI_API_KEY",
 357 |             )  # XXX: for backward compatibility, deprecate soon
 358 |             or env.get(
 359 |                 "BBM_OPENAI_API_KEY",
 360 |             )  # suggest adding `BBM_` prefix for all the bilingual_book_maker ENVs.
 361 |         ):
 362 |             API_KEY = OPENAI_API_KEY
 363 |             # patch
 364 |         elif options.ollama_model:
 365 |             # any string is ok, can't be empty
 366 |             API_KEY = "ollama"
 367 |         else:
 368 |             raise Exception(
 369 |                 "OpenAI API key not provided, please google how to obtain it",
 370 |             )
 371 |     elif options.model == "caiyun":
 372 |         API_KEY = options.caiyun_key or env.get("BBM_CAIYUN_API_KEY")
 373 |         if not API_KEY:
 374 |             raise Exception("Please provide caiyun key")
 375 |     elif options.model == "deepl":
 376 |         API_KEY = options.deepl_key or env.get("BBM_DEEPL_API_KEY")
 377 |         if not API_KEY:
 378 |             raise Exception("Please provide deepl key")
 379 |     elif options.model.startswith("claude"):
 380 |         API_KEY = options.claude_key or env.get("BBM_CLAUDE_API_KEY")
 381 |         if not API_KEY:
 382 |             raise Exception("Please provide claude key")
 383 |     elif options.model == "customapi":
 384 |         API_KEY = options.custom_api or env.get("BBM_CUSTOM_API")
 385 |         if not API_KEY:
 386 |             raise Exception("Please provide custom translate api")
 387 |     elif options.model in ["gemini", "geminipro"]:
 388 |         API_KEY = options.gemini_key or env.get("BBM_GOOGLE_GEMINI_KEY")
 389 |     elif options.model == "groq":
 390 |         API_KEY = options.groq_key or env.get("BBM_GROQ_API_KEY")
 391 |     elif options.model == "xai":
 392 |         API_KEY = options.xai_key or env.get("BBM_XAI_API_KEY")
 393 |     else:
 394 |         API_KEY = ""
 395 | 
 396 |     if options.book_from == "kobo":
 397 |         from book_maker import obok
 398 | 
 399 |         device_path = options.device_path
 400 |         if device_path is None:
 401 |             raise Exception(
 402 |                 "Device path is not given, please specify the path by --device_path <DEVICE_PATH>",
 403 |             )
 404 |         options.book_name = obok.cli_main(device_path)
 405 | 
 406 |     book_type = options.book_name.split(".")[-1]
 407 |     support_type_list = list(BOOK_LOADER_DICT.keys())
 408 |     if book_type not in support_type_list:
 409 |         raise Exception(
 410 |             f"now only support files of these formats: {','.join(support_type_list)}",
 411 |         )
 412 | 
 413 |     if options.block_size > 0 and not options.single_translate:
 414 |         raise Exception(
 415 |             "block_size must be used with `--single_translate` because it disturbs the original format",
 416 |         )
 417 | 
 418 |     book_loader = BOOK_LOADER_DICT.get(book_type)
 419 |     assert book_loader is not None, "unsupported loader"
 420 |     language = options.language
 421 |     if options.language in LANGUAGES:
 422 |         # use the value for prompt
 423 |         language = LANGUAGES.get(language, language)
 424 | 
 425 |     # change api_base for issue #42
 426 |     model_api_base = options.api_base
 427 | 
 428 |     if options.ollama_model and not model_api_base:
 429 |         # ollama default api_base
 430 |         model_api_base = "http://localhost:11434/v1"
 431 | 
 432 |     e = book_loader(
 433 |         options.book_name,
 434 |         translate_model,
 435 |         API_KEY,
 436 |         options.resume,
 437 |         language=language,
 438 |         model_api_base=model_api_base,
 439 |         is_test=options.test,
 440 |         test_num=options.test_num,
 441 |         prompt_config=parse_prompt_arg(options.prompt_arg),
 442 |         single_translate=options.single_translate,
 443 |         context_flag=options.context_flag,
 444 |         context_paragraph_limit=options.context_paragraph_limit,
 445 |         temperature=options.temperature,
 446 |     )
 447 |     # other options
 448 |     if options.allow_navigable_strings:
 449 |         e.allow_navigable_strings = True
 450 |     if options.translate_tags:
 451 |         e.translate_tags = options.translate_tags
 452 |     if options.exclude_translate_tags:
 453 |         e.exclude_translate_tags = options.exclude_translate_tags
 454 |     if options.exclude_filelist:
 455 |         e.exclude_filelist = options.exclude_filelist
 456 |     if options.only_filelist:
 457 |         e.only_filelist = options.only_filelist
 458 |     if options.accumulated_num > 1:
 459 |         e.accumulated_num = options.accumulated_num
 460 |     if options.translation_style:
 461 |         e.translation_style = options.translation_style
 462 |     if options.batch_size:
 463 |         e.batch_size = options.batch_size
 464 |     if options.retranslate:
 465 |         e.retranslate = options.retranslate
 466 |     if options.deployment_id:
 467 |         # only work for ChatGPT api for now
 468 |         # later maybe support others
 469 |         assert options.model in [
 470 |             "chatgptapi",
 471 |             "gpt4",
 472 |             "gpt4omini",
 473 |             "gpt4o",
 474 |         ], "only support chatgptapi for deployment_id"
 475 |         if not options.api_base:
 476 |             raise ValueError("`api_base` must be provided when using `deployment_id`")
 477 |         e.translate_model.set_deployment_id(options.deployment_id)
 478 |     if options.model in ("openai", "groq"):
 479 |         # Currently only supports `openai` when you also have --model_list set
 480 |         if options.model_list:
 481 |             e.translate_model.set_model_list(options.model_list.split(","))
 482 |         else:
 483 |             raise ValueError(
 484 |                 "When using `openai` model, you must also provide `--model_list`. For default model sets use `--model chatgptapi` or `--model gpt4` or `--model gpt4omini`",
 485 |             )
 486 |     # TODO refactor, quick fix for gpt4 model
 487 |     if options.model == "chatgptapi":
 488 |         if options.ollama_model:
 489 |             e.translate_model.set_gpt35_models(ollama_model=options.ollama_model)
 490 |         else:
 491 |             e.translate_model.set_gpt35_models()
 492 |     if options.model == "gpt4":
 493 |         e.translate_model.set_gpt4_models()
 494 |     if options.model == "gpt4omini":
 495 |         e.translate_model.set_gpt4omini_models()
 496 |     if options.model == "gpt4o":
 497 |         e.translate_model.set_gpt4o_models()
 498 |     if options.model.startswith("claude-"):
 499 |         e.translate_model.set_claude_model(options.model)
 500 |     if options.block_size > 0:
 501 |         e.block_size = options.block_size
 502 |     if options.batch_flag:
 503 |         e.batch_flag = options.batch_flag
 504 |     if options.batch_use_flag:
 505 |         e.batch_use_flag = options.batch_use_flag
 506 | 
 507 |     if options.model in ("gemini", "geminipro"):
 508 |         e.translate_model.set_interval(options.interval)
 509 |     if options.model == "gemini":
 510 |         if options.model_list:
 511 |             e.translate_model.set_model_list(options.model_list.split(","))
 512 |         else:
 513 |             e.translate_model.set_geminiflash_models()
 514 |     if options.model == "geminipro":
 515 |         e.translate_model.set_geminipro_models()
 516 | 
 517 |     e.make_bilingual_book()
 518 | 
 519 | 
 520 | if __name__ == "__main__":
 521 |     main()

```

`/Users/arthrod/Library/CloudStorage/GoogleDrive-arthursrodrigues@gmail.com/My Drive/acode/atemp-drive/bilingual_book_maker/book_maker/utils.py`:

```py
   1 | import tiktoken
   2 | 
   3 | # Borrowed from : https://github.com/openai/whisper
   4 | LANGUAGES = {
   5 |     "en": "english",
   6 |     "zh-hans": "simplified chinese",
   7 |     "zh": "simplified chinese",
   8 |     "zh-hant": "traditional chinese",
   9 |     "zh-yue": "cantonese",
  10 |     "de": "german",
  11 |     "es": "spanish",
  12 |     "ru": "russian",
  13 |     "ko": "korean",
  14 |     "fr": "french",
  15 |     "ja": "japanese",
  16 |     "pt": "portuguese",
  17 |     "tr": "turkish",
  18 |     "pl": "polish",
  19 |     "ca": "catalan",
  20 |     "nl": "dutch",
  21 |     "ar": "arabic",
  22 |     "sv": "swedish",
  23 |     "it": "italian",
  24 |     "id": "indonesian",
  25 |     "hi": "hindi",
  26 |     "fi": "finnish",
  27 |     "vi": "vietnamese",
  28 |     "he": "hebrew",
  29 |     "uk": "ukrainian",
  30 |     "el": "greek",
  31 |     "ms": "malay",
  32 |     "cs": "czech",
  33 |     "ro": "romanian",
  34 |     "da": "danish",
  35 |     "hu": "hungarian",
  36 |     "ta": "tamil",
  37 |     "no": "norwegian",
  38 |     "th": "thai",
  39 |     "ur": "urdu",
  40 |     "hr": "croatian",
  41 |     "bg": "bulgarian",
  42 |     "lt": "lithuanian",
  43 |     "la": "latin",
  44 |     "mi": "maori",
  45 |     "ml": "malayalam",
  46 |     "cy": "welsh",
  47 |     "sk": "slovak",
  48 |     "te": "telugu",
  49 |     "fa": "persian",
  50 |     "lv": "latvian",
  51 |     "bn": "bengali",
  52 |     "sr": "serbian",
  53 |     "az": "azerbaijani",
  54 |     "sl": "slovenian",
  55 |     "kn": "kannada",
  56 |     "et": "estonian",
  57 |     "mk": "macedonian",
  58 |     "br": "breton",
  59 |     "eu": "basque",
  60 |     "is": "icelandic",
  61 |     "hy": "armenian",
  62 |     "ne": "nepali",
  63 |     "mn": "mongolian",
  64 |     "bs": "bosnian",
  65 |     "kk": "kazakh",
  66 |     "sq": "albanian",
  67 |     "sw": "swahili",
  68 |     "gl": "galician",
  69 |     "mr": "marathi",
  70 |     "pa": "punjabi",
  71 |     "si": "sinhala",
  72 |     "km": "khmer",
  73 |     "sn": "shona",
  74 |     "yo": "yoruba",
  75 |     "so": "somali",
  76 |     "af": "afrikaans",
  77 |     "oc": "occitan",
  78 |     "ka": "georgian",
  79 |     "be": "belarusian",
  80 |     "tg": "tajik",
  81 |     "sd": "sindhi",
  82 |     "gu": "gujarati",
  83 |     "am": "amharic",
  84 |     "yi": "yiddish",
  85 |     "lo": "lao",
  86 |     "uz": "uzbek",
  87 |     "fo": "faroese",
  88 |     "ht": "haitian creole",
  89 |     "ps": "pashto",
  90 |     "tk": "turkmen",
  91 |     "nn": "nynorsk",
  92 |     "mt": "maltese",
  93 |     "sa": "sanskrit",
  94 |     "lb": "luxembourgish",
  95 |     "my": "myanmar",
  96 |     "bo": "tibetan",
  97 |     "tl": "tagalog",
  98 |     "mg": "malagasy",
  99 |     "as": "assamese",
 100 |     "tt": "tatar",
 101 |     "haw": "hawaiian",
 102 |     "ln": "lingala",
 103 |     "ha": "hausa",
 104 |     "ba": "bashkir",
 105 |     "jw": "javanese",
 106 |     "su": "sundanese",
 107 | }
 108 | 
 109 | # language code lookup by name, with a few language aliases
 110 | TO_LANGUAGE_CODE = {
 111 |     **{language: code for code, language in LANGUAGES.items()},
 112 |     "burmese": "my",
 113 |     "valencian": "ca",
 114 |     "flemish": "nl",
 115 |     "haitian": "ht",
 116 |     "letzeburgesch": "lb",
 117 |     "pushto": "ps",
 118 |     "panjabi": "pa",
 119 |     "moldavian": "ro",
 120 |     "moldovan": "ro",
 121 |     "sinhalese": "si",
 122 |     "castilian": "es",
 123 | }
 124 | 
 125 | 
 126 | def prompt_config_to_kwargs(prompt_config):
 127 |     prompt_config = prompt_config or {}
 128 |     return dict(
 129 |         prompt_template=prompt_config.get("user", None),
 130 |         prompt_sys_msg=prompt_config.get("system", None),
 131 |     )
 132 | 
 133 | 
 134 | # ref: https://platform.openai.com/docs/guides/chat/introduction
 135 | def num_tokens_from_text(text, model="gpt-3.5-turbo-0301"):
 136 |     messages = (
 137 |         {
 138 |             "role": "user",
 139 |             "content": text,
 140 |         },
 141 |     )
 142 | 
 143 |     """Returns the number of tokens used by a list of messages."""
 144 |     try:
 145 |         encoding = tiktoken.encoding_for_model(model)
 146 |     except KeyError:
 147 |         encoding = tiktoken.get_encoding("cl100k_base")
 148 |     if model == "gpt-3.5-turbo-0301":  # note: future models may deviate from this
 149 |         num_tokens = 0
 150 |         for message in messages:
 151 |             num_tokens += (
 152 |                 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
 153 |             )
 154 |             for key, value in message.items():
 155 |                 num_tokens += len(encoding.encode(value))
 156 |                 if key == "name":  # if there's a name, the role is omitted
 157 |                     num_tokens += -1  # role is always required and always 1 token
 158 |         num_tokens += 2  # every reply is primed with <im_start>assistant
 159 |         return num_tokens
 160 |     else:
 161 |         raise NotImplementedError(
 162 |             f"""num_tokens_from_messages() is not presently implemented for model {model}.
 163 |   See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens."""
 164 |         )

```

`/Users/arthrod/Library/CloudStorage/GoogleDrive-arthursrodrigues@gmail.com/My Drive/acode/atemp-drive/bilingual_book_maker/book_maker/loader/srt_loader.py`:

```py
   1 | """
   2 | inspired by: https://github.com/jesselau76/srt-gpt-translator, MIT License
   3 | """
   4 | 
   5 | import re
   6 | import sys
   7 | from pathlib import Path
   8 | 
   9 | from book_maker.utils import prompt_config_to_kwargs
  10 | 
  11 | from .base_loader import BaseBookLoader
  12 | 
  13 | 
  14 | class SRTBookLoader(BaseBookLoader):
  15 |     def __init__(
  16 |         self,
  17 |         srt_name,
  18 |         model,
  19 |         key,
  20 |         resume,
  21 |         language,
  22 |         model_api_base=None,
  23 |         is_test=False,
  24 |         test_num=5,
  25 |         prompt_config=None,
  26 |         single_translate=False,
  27 |         context_flag=False,
  28 |         context_paragraph_limit=0,
  29 |         temperature=1.0,
  30 |     ) -> None:
  31 |         self.srt_name = srt_name
  32 |         self.translate_model = model(
  33 |             key,
  34 |             language,
  35 |             api_base=model_api_base,
  36 |             temperature=temperature,
  37 |             **prompt_config_to_kwargs(
  38 |                 {
  39 |                     "system": "You are a srt subtitle file translator.",
  40 |                     "user": "Translate the following subtitle text into {language}, but keep the subtitle number and timeline and newlines unchanged: \n{text}",
  41 |                 }
  42 |             ),
  43 |         )
  44 |         self.is_test = is_test
  45 |         self.p_to_save = []
  46 |         self.bilingual_result = []
  47 |         self.bilingual_temp_result = []
  48 |         self.test_num = test_num
  49 |         self.accumulated_num = 1
  50 |         self.blocks = []
  51 |         self.single_translate = single_translate
  52 | 
  53 |         self.resume = resume
  54 |         self.bin_path = f"{Path(srt_name).parent}/.{Path(srt_name).stem}.temp.bin"
  55 |         if self.resume:
  56 |             self.load_state()
  57 | 
  58 |     def _make_new_book(self, book):
  59 |         pass
  60 | 
  61 |     def _parse_srt(self, srt_text):
  62 |         blocks = re.split("\n\s*\n", srt_text)
  63 | 
  64 |         final_blocks = []
  65 |         new_block = {}
  66 |         for i in range(0, len(blocks)):
  67 |             block = blocks[i]
  68 |             if block.strip() == "":
  69 |                 continue
  70 | 
  71 |             lines = block.strip().splitlines()
  72 |             new_block["number"] = lines[0].strip()
  73 |             timestamp = lines[1].strip()
  74 |             new_block["time"] = timestamp
  75 |             text = "\n".join(lines[2:]).strip()
  76 |             new_block["text"] = text
  77 |             final_blocks.append(new_block)
  78 |             new_block = {}
  79 | 
  80 |         return final_blocks
  81 | 
  82 |     def _get_block_text(self, block):
  83 |         return f"{block['number']}\n{block['time']}\n{block['text']}"
  84 | 
  85 |     def _get_block_except_text(self, block):
  86 |         return f"{block['number']}\n{block['time']}"
  87 | 
  88 |     def _concat_blocks(self, sliced_text: str, text: str):
  89 |         return f"{sliced_text}\n\n{text}" if sliced_text else text
  90 | 
  91 |     def _get_block_translate(self, block):
  92 |         return f"{block['number']}\n{block['text']}"
  93 | 
  94 |     def _get_block_from(self, text):
  95 |         text = text.strip()
  96 |         if not text:
  97 |             return {}
  98 | 
  99 |         block = text.splitlines()
 100 |         if len(block) < 2:
 101 |             return {"number": block[0], "text": ""}
 102 | 
 103 |         return {"number": block[0], "text": "\n".join(block[1:])}
 104 | 
 105 |     def _get_blocks_from(self, translate: str):
 106 |         if not translate:
 107 |             return []
 108 | 
 109 |         blocks = []
 110 |         blocks_text = translate.strip().split("\n\n")
 111 |         for text in blocks_text:
 112 |             blocks.append(self._get_block_from(text))
 113 | 
 114 |         return blocks
 115 | 
 116 |     def _check_blocks(self, translate_blocks, origin_blocks):
 117 |         """
 118 |         Check if the translated blocks match the original text, with only a simple check of the beginning numbers.
 119 |         """
 120 |         if len(translate_blocks) != len(origin_blocks):
 121 |             return False
 122 | 
 123 |         for t in zip(translate_blocks, origin_blocks):
 124 |             i = 0
 125 |             try:
 126 |                 i = int(t[0].get("number", 0))
 127 |             except ValueError:
 128 |                 m = re.search(r"\s*\d+", t[0].get("number"))
 129 |                 if m:
 130 |                     i = int(m.group())
 131 | 
 132 |             j = int(t[1].get("number", -1))
 133 |             if i != j:
 134 |                 print(f"check failed: {i}!={j}")
 135 |                 return False
 136 | 
 137 |         return True
 138 | 
 139 |     def _get_sliced_list(self):
 140 |         sliced_list = []
 141 |         sliced_text = ""
 142 |         begin_index = 0
 143 |         for i, block in enumerate(self.blocks):
 144 |             text = self._get_block_translate(block)
 145 |             if not text:
 146 |                 continue
 147 | 
 148 |             if len(sliced_text + text) < self.accumulated_num:
 149 |                 sliced_text = self._concat_blocks(sliced_text, text)
 150 |             else:
 151 |                 if sliced_text:
 152 |                     sliced_list.append((begin_index, i, sliced_text))
 153 |                 sliced_text = text
 154 |                 begin_index = i
 155 | 
 156 |         sliced_list.append((begin_index, len(self.blocks), sliced_text))
 157 |         return sliced_list
 158 | 
 159 |     def make_bilingual_book(self):
 160 |         if self.accumulated_num > 512:
 161 |             print(f"{self.accumulated_num} is too large, shrink it to 512.")
 162 |             self.accumulated_num = 512
 163 | 
 164 |         try:
 165 |             with open(f"{self.srt_name}", encoding="utf-8") as f:
 166 |                 self.blocks = self._parse_srt(f.read())
 167 |         except Exception as e:
 168 |             raise Exception("can not load file") from e
 169 | 
 170 |         index = 0
 171 |         p_to_save_len = len(self.p_to_save)
 172 | 
 173 |         try:
 174 |             sliced_list = self._get_sliced_list()
 175 | 
 176 |             for sliced in sliced_list:
 177 |                 begin, end, text = sliced
 178 | 
 179 |                 if not self.resume or index + (end - begin) > p_to_save_len:
 180 |                     if index < p_to_save_len:
 181 |                         self.p_to_save = self.p_to_save[:index]
 182 | 
 183 |                     try:
 184 |                         temp = self.translate_model.translate(text)
 185 |                     except Exception as e:
 186 |                         print(e)
 187 |                         raise Exception("Something is wrong when translate") from e
 188 | 
 189 |                     translated_blocks = self._get_blocks_from(temp)
 190 | 
 191 |                     if self.accumulated_num > 1:
 192 |                         if not self._check_blocks(
 193 |                             translated_blocks, self.blocks[begin:end]
 194 |                         ):
 195 |                             translated_blocks = []
 196 |                             # try to translate one by one, so don't accumulate too much
 197 |                             print(
 198 |                                 f"retry it one by one:  {self.blocks[begin]['number']} - {self.blocks[end - 1]['number']}"
 199 |                             )
 200 |                             for block in self.blocks[begin:end]:
 201 |                                 try:
 202 |                                     temp = self.translate_model.translate(
 203 |                                         self._get_block_translate(block)
 204 |                                     )
 205 |                                 except Exception as e:
 206 |                                     print(e)
 207 |                                     raise Exception(
 208 |                                         "Something is wrong when translate"
 209 |                                     ) from e
 210 |                                 translated_blocks.append(self._get_block_from(temp))
 211 | 
 212 |                             if not self._check_blocks(
 213 |                                 translated_blocks, self.blocks[begin:end]
 214 |                             ):
 215 |                                 raise Exception(
 216 |                                     f"retry failed, adjust the srt manually."
 217 |                                 )
 218 | 
 219 |                     for i, block in enumerate(translated_blocks):
 220 |                         text = block.get("text", "")
 221 |                         self.p_to_save.append(text)
 222 |                         if self.single_translate:
 223 |                             self.bilingual_result.append(
 224 |                                 f"{self._get_block_except_text(self.blocks[begin + i])}\n{text}"
 225 |                             )
 226 |                         else:
 227 |                             self.bilingual_result.append(
 228 |                                 f"{self._get_block_text(self.blocks[begin + i])}\n{text}"
 229 |                             )
 230 |                 else:
 231 |                     for i, block in enumerate(self.blocks[begin:end]):
 232 |                         text = self.p_to_save[begin + i]
 233 |                         if self.single_translate:
 234 |                             self.bilingual_result.append(
 235 |                                 f"{self._get_block_except_text(self.blocks[begin + i])}\n{text}"
 236 |                             )
 237 |                         else:
 238 |                             self.bilingual_result.append(
 239 |                                 f"{self._get_block_text(self.blocks[begin + i])}\n{text}"
 240 |                             )
 241 | 
 242 |                 index += end - begin
 243 |                 if self.is_test and index > self.test_num:
 244 |                     break
 245 | 
 246 |             self.save_file(
 247 |                 f"{Path(self.srt_name).parent}/{Path(self.srt_name).stem}_bilingual.srt",
 248 |                 self.bilingual_result,
 249 |             )
 250 | 
 251 |         except (KeyboardInterrupt, Exception) as e:
 252 |             print(e)
 253 |             print("you can resume it next time")
 254 |             self._save_progress()
 255 |             self._save_temp_book()
 256 |             sys.exit(0)
 257 | 
 258 |     def _save_temp_book(self):
 259 |         for i, block in enumerate(self.blocks):
 260 |             if i < len(self.p_to_save):
 261 |                 text = self.p_to_save[i]
 262 |                 self.bilingual_temp_result.append(
 263 |                     f"{self._get_block_text(block)}\n{text}"
 264 |                 )
 265 |             else:
 266 |                 self.bilingual_temp_result.append(f"{self._get_block_text(block)}\n")
 267 | 
 268 |         self.save_file(
 269 |             f"{Path(self.srt_name).parent}/{Path(self.srt_name).stem}_bilingual_temp.srt",
 270 |             self.bilingual_temp_result,
 271 |         )
 272 | 
 273 |     def _save_progress(self):
 274 |         try:
 275 |             with open(self.bin_path, "w", encoding="utf-8") as f:
 276 |                 f.write("===".join(self.p_to_save))
 277 |         except:
 278 |             raise Exception("can not save resume file")
 279 | 
 280 |     def load_state(self):
 281 |         try:
 282 |             with open(self.bin_path, encoding="utf-8") as f:
 283 |                 text = f.read()
 284 |                 if text:
 285 |                     self.p_to_save = text.split("===")
 286 |                 else:
 287 |                     self.p_to_save = []
 288 | 
 289 |         except Exception as e:
 290 |             raise Exception("can not load resume file") from e
 291 | 
 292 |     def save_file(self, book_path, content):
 293 |         try:
 294 |             with open(book_path, "w", encoding="utf-8") as f:
 295 |                 f.write("\n\n".join(content))
 296 |         except:
 297 |             raise Exception("can not save file")

```

`/Users/arthrod/Library/CloudStorage/GoogleDrive-arthursrodrigues@gmail.com/My Drive/acode/atemp-drive/bilingual_book_maker/book_maker/loader/__init__.py`:

```py
   1 | from book_maker.loader.epub_loader import EPUBBookLoader
   2 | from book_maker.loader.txt_loader import TXTBookLoader
   3 | from book_maker.loader.srt_loader import SRTBookLoader
   4 | from book_maker.loader.md_loader import MarkdownBookLoader
   5 | 
   6 | BOOK_LOADER_DICT = {
   7 |     "epub": EPUBBookLoader,
   8 |     "txt": TXTBookLoader,
   9 |     "srt": SRTBookLoader,
  10 |     "md": MarkdownBookLoader,
  11 |     # TODO add more here
  12 | }

```

`/Users/arthrod/Library/CloudStorage/GoogleDrive-arthursrodrigues@gmail.com/My Drive/acode/atemp-drive/bilingual_book_maker/book_maker/loader/txt_loader.py`:

```py
   1 | import sys
   2 | from pathlib import Path
   3 | 
   4 | from book_maker.utils import prompt_config_to_kwargs
   5 | 
   6 | from .base_loader import BaseBookLoader
   7 | 
   8 | 
   9 | class TXTBookLoader(BaseBookLoader):
  10 |     def __init__(
  11 |         self,
  12 |         txt_name,
  13 |         model,
  14 |         key,
  15 |         resume,
  16 |         language,
  17 |         model_api_base=None,
  18 |         is_test=False,
  19 |         test_num=5,
  20 |         prompt_config=None,
  21 |         single_translate=False,
  22 |         context_flag=False,
  23 |         context_paragraph_limit=0,
  24 |         temperature=1.0,
  25 |     ) -> None:
  26 |         self.txt_name = txt_name
  27 |         self.translate_model = model(
  28 |             key,
  29 |             language,
  30 |             api_base=model_api_base,
  31 |             temperature=temperature,
  32 |             **prompt_config_to_kwargs(prompt_config),
  33 |         )
  34 |         self.is_test = is_test
  35 |         self.p_to_save = []
  36 |         self.bilingual_result = []
  37 |         self.bilingual_temp_result = []
  38 |         self.test_num = test_num
  39 |         self.batch_size = 10
  40 |         self.single_translate = single_translate
  41 | 
  42 |         try:
  43 |             with open(f"{txt_name}", encoding="utf-8") as f:
  44 |                 self.origin_book = f.read().splitlines()
  45 | 
  46 |         except Exception as e:
  47 |             raise Exception("can not load file") from e
  48 | 
  49 |         self.resume = resume
  50 |         self.bin_path = f"{Path(txt_name).parent}/.{Path(txt_name).stem}.temp.bin"
  51 |         if self.resume:
  52 |             self.load_state()
  53 | 
  54 |     @staticmethod
  55 |     def _is_special_text(text):
  56 |         return text.isdigit() or text.isspace() or len(text) == 0
  57 | 
  58 |     def _make_new_book(self, book):
  59 |         pass
  60 | 
  61 |     def make_bilingual_book(self):
  62 |         index = 0
  63 |         p_to_save_len = len(self.p_to_save)
  64 | 
  65 |         try:
  66 |             sliced_list = [
  67 |                 self.origin_book[i : i + self.batch_size]
  68 |                 for i in range(0, len(self.origin_book), self.batch_size)
  69 |             ]
  70 |             for i in sliced_list:
  71 |                 # fix the format thanks https://github.com/tudoujunha
  72 |                 batch_text = "\n".join(i)
  73 |                 if self._is_special_text(batch_text):
  74 |                     continue
  75 |                 if not self.resume or index >= p_to_save_len:
  76 |                     try:
  77 |                         temp = self.translate_model.translate(batch_text)
  78 |                     except Exception as e:
  79 |                         print(e)
  80 |                         raise Exception("Something is wrong when translate") from e
  81 |                     self.p_to_save.append(temp)
  82 |                     if not self.single_translate:
  83 |                         self.bilingual_result.append(batch_text)
  84 |                     self.bilingual_result.append(temp)
  85 |                 index += self.batch_size
  86 |                 if self.is_test and index > self.test_num:
  87 |                     break
  88 | 
  89 |             self.save_file(
  90 |                 f"{Path(self.txt_name).parent}/{Path(self.txt_name).stem}_bilingual.txt",
  91 |                 self.bilingual_result,
  92 |             )
  93 | 
  94 |         except (KeyboardInterrupt, Exception) as e:
  95 |             print(e)
  96 |             print("you can resume it next time")
  97 |             self._save_progress()
  98 |             self._save_temp_book()
  99 |             sys.exit(0)
 100 | 
 101 |     def _save_temp_book(self):
 102 |         index = 0
 103 |         sliced_list = [
 104 |             self.origin_book[i : i + self.batch_size]
 105 |             for i in range(0, len(self.origin_book), self.batch_size)
 106 |         ]
 107 | 
 108 |         for i in range(len(sliced_list)):
 109 |             batch_text = "".join(sliced_list[i])
 110 |             self.bilingual_temp_result.append(batch_text)
 111 |             if self._is_special_text(self.origin_book[i]):
 112 |                 continue
 113 |             if index < len(self.p_to_save):
 114 |                 self.bilingual_temp_result.append(self.p_to_save[index])
 115 |             index += 1
 116 | 
 117 |         self.save_file(
 118 |             f"{Path(self.txt_name).parent}/{Path(self.txt_name).stem}_bilingual_temp.txt",
 119 |             self.bilingual_temp_result,
 120 |         )
 121 | 
 122 |     def _save_progress(self):
 123 |         try:
 124 |             with open(self.bin_path, "w", encoding="utf-8") as f:
 125 |                 f.write("\n".join(self.p_to_save))
 126 |         except:
 127 |             raise Exception("can not save resume file")
 128 | 
 129 |     def load_state(self):
 130 |         try:
 131 |             with open(self.bin_path, encoding="utf-8") as f:
 132 |                 self.p_to_save = f.read().splitlines()
 133 |         except Exception as e:
 134 |             raise Exception("can not load resume file") from e
 135 | 
 136 |     def save_file(self, book_path, content):
 137 |         try:
 138 |             with open(book_path, "w", encoding="utf-8") as f:
 139 |                 f.write("\n".join(content))
 140 |         except:
 141 |             raise Exception("can not save file")

```

`/Users/arthrod/Library/CloudStorage/GoogleDrive-arthursrodrigues@gmail.com/My Drive/acode/atemp-drive/bilingual_book_maker/book_maker/loader/md_loader.py`:

```py
   1 | import sys
   2 | from pathlib import Path
   3 | 
   4 | from book_maker.utils import prompt_config_to_kwargs
   5 | 
   6 | from .base_loader import BaseBookLoader
   7 | 
   8 | 
   9 | class MarkdownBookLoader(BaseBookLoader):
  10 |     def __init__(
  11 |         self,
  12 |         md_name,
  13 |         model,
  14 |         key,
  15 |         resume,
  16 |         language,
  17 |         model_api_base=None,
  18 |         is_test=False,
  19 |         test_num=5,
  20 |         prompt_config=None,
  21 |         single_translate=False,
  22 |         context_flag=False,
  23 |         context_paragraph_limit=0,
  24 |         temperature=1.0,
  25 |     ) -> None:
  26 |         self.md_name = md_name
  27 |         self.translate_model = model(
  28 |             key,
  29 |             language,
  30 |             api_base=model_api_base,
  31 |             temperature=temperature,
  32 |             **prompt_config_to_kwargs(prompt_config),
  33 |         )
  34 |         self.is_test = is_test
  35 |         self.p_to_save = []
  36 |         self.bilingual_result = []
  37 |         self.bilingual_temp_result = []
  38 |         self.test_num = test_num
  39 |         self.batch_size = 10
  40 |         self.single_translate = single_translate
  41 |         self.md_paragraphs = []
  42 | 
  43 |         try:
  44 |             with open(f"{md_name}", encoding="utf-8") as f:
  45 |                 self.origin_book = f.read().splitlines()
  46 | 
  47 |         except Exception as e:
  48 |             raise Exception("can not load file") from e
  49 | 
  50 |         self.resume = resume
  51 |         self.bin_path = f"{Path(md_name).parent}/.{Path(md_name).stem}.temp.bin"
  52 |         if self.resume:
  53 |             self.load_state()
  54 | 
  55 |         self.process_markdown_content()
  56 | 
  57 |     def process_markdown_content(self):
  58 |         """将原始内容处理成 markdown 段落"""
  59 |         current_paragraph = []
  60 |         for line in self.origin_book:
  61 |             # 如果是空行且当前段落不为空，保存当前段落
  62 |             if not line.strip() and current_paragraph:
  63 |                 self.md_paragraphs.append("\n".join(current_paragraph))
  64 |                 current_paragraph = []
  65 |             # 如果是标题行，单独作为一个段落
  66 |             elif line.strip().startswith("#"):
  67 |                 if current_paragraph:
  68 |                     self.md_paragraphs.append("\n".join(current_paragraph))
  69 |                     current_paragraph = []
  70 |                 self.md_paragraphs.append(line)
  71 |             # 其他情况，添加到当前段落
  72 |             else:
  73 |                 current_paragraph.append(line)
  74 | 
  75 |         # 处理最后一个段落
  76 |         if current_paragraph:
  77 |             self.md_paragraphs.append("\n".join(current_paragraph))
  78 | 
  79 |     @staticmethod
  80 |     def _is_special_text(text):
  81 |         return text.isdigit() or text.isspace() or len(text) == 0
  82 | 
  83 |     def _make_new_book(self, book):
  84 |         pass
  85 | 
  86 |     def make_bilingual_book(self):
  87 |         index = 0
  88 |         p_to_save_len = len(self.p_to_save)
  89 | 
  90 |         try:
  91 |             sliced_list = [
  92 |                 self.md_paragraphs[i : i + self.batch_size]
  93 |                 for i in range(0, len(self.md_paragraphs), self.batch_size)
  94 |             ]
  95 |             for paragraphs in sliced_list:
  96 |                 batch_text = "\n\n".join(paragraphs)
  97 |                 if self._is_special_text(batch_text):
  98 |                     continue
  99 |                 if not self.resume or index >= p_to_save_len:
 100 |                     try:
 101 |                         max_retries = 3
 102 |                         retry_count = 0
 103 |                         while retry_count < max_retries:
 104 |                             try:
 105 |                                 temp = self.translate_model.translate(batch_text)
 106 |                                 break
 107 |                             except AttributeError as ae:
 108 |                                 print(f"翻译出错: {ae}")
 109 |                                 retry_count += 1
 110 |                                 if retry_count == max_retries:
 111 |                                     raise Exception("翻译模型初始化失败") from ae
 112 |                     except Exception as e:
 113 |                         print(f"翻译过程中出错: {e}")
 114 |                         raise Exception("翻译过程中出现错误") from e
 115 | 
 116 |                     self.p_to_save.append(temp)
 117 |                     if not self.single_translate:
 118 |                         self.bilingual_result.append(batch_text)
 119 |                     self.bilingual_result.append(temp)
 120 |                 index += self.batch_size
 121 |                 if self.is_test and index > self.test_num:
 122 |                     break
 123 | 
 124 |             self.save_file(
 125 |                 f"{Path(self.md_name).parent}/{Path(self.md_name).stem}_bilingual.md",
 126 |                 self.bilingual_result,
 127 |             )
 128 | 
 129 |         except (KeyboardInterrupt, Exception) as e:
 130 |             print(f"发生错误: {e}")
 131 |             print("程序将保存进度，您可以稍后继续")
 132 |             self._save_progress()
 133 |             self._save_temp_book()
 134 |             sys.exit(1)  # 使用非零退出码表示错误
 135 | 
 136 |     def _save_temp_book(self):
 137 |         index = 0
 138 |         sliced_list = [
 139 |             self.origin_book[i : i + self.batch_size]
 140 |             for i in range(0, len(self.origin_book), self.batch_size)
 141 |         ]
 142 | 
 143 |         for i in range(len(sliced_list)):
 144 |             batch_text = "".join(sliced_list[i])
 145 |             self.bilingual_temp_result.append(batch_text)
 146 |             if self._is_special_text(self.origin_book[i]):
 147 |                 continue
 148 |             if index < len(self.p_to_save):
 149 |                 self.bilingual_temp_result.append(self.p_to_save[index])
 150 |             index += 1
 151 | 
 152 |         self.save_file(
 153 |             f"{Path(self.md_name).parent}/{Path(self.md_name).stem}_bilingual_temp.txt",
 154 |             self.bilingual_temp_result,
 155 |         )
 156 | 
 157 |     def _save_progress(self):
 158 |         try:
 159 |             with open(self.bin_path, "w", encoding="utf-8") as f:
 160 |                 f.write("\n".join(self.p_to_save))
 161 |         except:
 162 |             raise Exception("can not save resume file")
 163 | 
 164 |     def load_state(self):
 165 |         try:
 166 |             with open(self.bin_path, encoding="utf-8") as f:
 167 |                 self.p_to_save = f.read().splitlines()
 168 |         except Exception as e:
 169 |             raise Exception("can not load resume file") from e
 170 | 
 171 |     def save_file(self, book_path, content):
 172 |         try:
 173 |             with open(book_path, "w", encoding="utf-8") as f:
 174 |                 f.write("\n".join(content))
 175 |         except:
 176 |             raise Exception("can not save file")

```

`/Users/arthrod/Library/CloudStorage/GoogleDrive-arthursrodrigues@gmail.com/My Drive/acode/atemp-drive/bilingual_book_maker/book_maker/loader/base_loader.py`:

```py
   1 | from abc import ABC, abstractmethod
   2 | 
   3 | 
   4 | class BaseBookLoader(ABC):
   5 |     @staticmethod
   6 |     def _is_special_text(text):
   7 |         return text.isdigit() or text.isspace()
   8 | 
   9 |     @abstractmethod
  10 |     def _make_new_book(self, book):
  11 |         pass
  12 | 
  13 |     @abstractmethod
  14 |     def make_bilingual_book(self):
  15 |         pass
  16 | 
  17 |     @abstractmethod
  18 |     def load_state(self):
  19 |         pass
  20 | 
  21 |     @abstractmethod
  22 |     def _save_temp_book(self):
  23 |         pass
  24 | 
  25 |     @abstractmethod
  26 |     def _save_progress(self):
  27 |         pass

```

`/Users/arthrod/Library/CloudStorage/GoogleDrive-arthursrodrigues@gmail.com/My Drive/acode/atemp-drive/bilingual_book_maker/book_maker/loader/helper.py`:

```py
   1 | import re
   2 | import backoff
   3 | import logging
   4 | from copy import copy
   5 | 
   6 | logging.basicConfig(level=logging.WARNING)
   7 | logger = logging.getLogger(__name__)
   8 | 
   9 | 
  10 | class EPUBBookLoaderHelper:
  11 |     def __init__(
  12 |         self, translate_model, accumulated_num, translation_style, context_flag
  13 |     ):
  14 |         self.translate_model = translate_model
  15 |         self.accumulated_num = accumulated_num
  16 |         self.translation_style = translation_style
  17 |         self.context_flag = context_flag
  18 | 
  19 |     def insert_trans(self, p, text, translation_style="", single_translate=False):
  20 |         if text is None:
  21 |             text = ""
  22 |         if (
  23 |             p.string is not None
  24 |             and p.string.replace(" ", "").strip() == text.replace(" ", "").strip()
  25 |         ):
  26 |             return
  27 |         new_p = copy(p)
  28 |         new_p.string = text
  29 |         if translation_style != "":
  30 |             new_p["style"] = translation_style
  31 |         p.insert_after(new_p)
  32 |         if single_translate:
  33 |             p.extract()
  34 | 
  35 |     @backoff.on_exception(
  36 |         backoff.expo,
  37 |         Exception,
  38 |         on_backoff=lambda details: logger.warning(f"retry backoff: {details}"),
  39 |         on_giveup=lambda details: logger.warning(f"retry abort: {details}"),
  40 |         jitter=None,
  41 |     )
  42 |     def translate_with_backoff(self, text, context_flag=False):
  43 |         return self.translate_model.translate(text, context_flag)
  44 | 
  45 |     def deal_new(self, p, wait_p_list, single_translate=False):
  46 |         self.deal_old(wait_p_list, single_translate, self.context_flag)
  47 |         self.insert_trans(
  48 |             p,
  49 |             shorter_result_link(self.translate_with_backoff(p.text, self.context_flag)),
  50 |             self.translation_style,
  51 |             single_translate,
  52 |         )
  53 | 
  54 |     def deal_old(self, wait_p_list, single_translate=False, context_flag=False):
  55 |         if not wait_p_list:
  56 |             return
  57 | 
  58 |         result_txt_list = self.translate_model.translate_list(wait_p_list)
  59 | 
  60 |         for i in range(len(wait_p_list)):
  61 |             if i < len(result_txt_list):
  62 |                 p = wait_p_list[i]
  63 |                 self.insert_trans(
  64 |                     p,
  65 |                     shorter_result_link(result_txt_list[i]),
  66 |                     self.translation_style,
  67 |                     single_translate,
  68 |                 )
  69 | 
  70 |         wait_p_list.clear()
  71 | 
  72 | 
  73 | url_pattern = r"(http[s]?://|www\.)+(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
  74 | 
  75 | 
  76 | def is_text_link(text):
  77 |     return bool(re.compile(url_pattern).match(text.strip()))
  78 | 
  79 | 
  80 | def is_text_tail_link(text, num=80):
  81 |     text = text.strip()
  82 |     pattern = r".*" + url_pattern + r"$"
  83 |     return bool(re.compile(pattern).match(text)) and len(text) < num
  84 | 
  85 | 
  86 | def shorter_result_link(text, num=20):
  87 |     match = re.search(url_pattern, text)
  88 | 
  89 |     if not match or len(match.group()) < num:
  90 |         return text
  91 | 
  92 |     return re.compile(url_pattern).sub("...", text)
  93 | 
  94 | 
  95 | def is_text_source(text):
  96 |     return text.strip().startswith("Source: ")
  97 | 
  98 | 
  99 | def is_text_list(text, num=80):
 100 |     text = text.strip()
 101 |     return re.match(r"^Listing\s*\d+", text) and len(text) < num
 102 | 
 103 | 
 104 | def is_text_figure(text, num=80):
 105 |     text = text.strip()
 106 |     return re.match(r"^Figure\s*\d+", text) and len(text) < num
 107 | 
 108 | 
 109 | def is_text_digit_and_space(s):
 110 |     for c in s:
 111 |         if not c.isdigit() and not c.isspace():
 112 |             return False
 113 |     return True
 114 | 
 115 | 
 116 | def is_text_isbn(s):
 117 |     pattern = r"^[Ee]?ISBN\s*\d[\d\s]*$"
 118 |     return bool(re.match(pattern, s))
 119 | 
 120 | 
 121 | def not_trans(s):
 122 |     return any(
 123 |         [
 124 |             is_text_link(s),
 125 |             is_text_tail_link(s),
 126 |             is_text_source(s),
 127 |             is_text_list(s),
 128 |             is_text_figure(s),
 129 |             is_text_digit_and_space(s),
 130 |             is_text_isbn(s),
 131 |         ]
 132 |     )

```

`/Users/arthrod/Library/CloudStorage/GoogleDrive-arthursrodrigues@gmail.com/My Drive/acode/atemp-drive/bilingual_book_maker/book_maker/loader/epub_loader.py`:

```py
   1 | import os
   2 | import pickle
   3 | import string
   4 | import sys
   5 | import time
   6 | from copy import copy
   7 | from pathlib import Path
   8 | 
   9 | from bs4 import BeautifulSoup as bs
  10 | from bs4 import Tag
  11 | from bs4.element import NavigableString
  12 | from ebooklib import ITEM_DOCUMENT, epub
  13 | from rich import print
  14 | from tqdm import tqdm
  15 | 
  16 | from book_maker.utils import num_tokens_from_text, prompt_config_to_kwargs
  17 | 
  18 | from .base_loader import BaseBookLoader
  19 | from .helper import EPUBBookLoaderHelper, is_text_link, not_trans
  20 | 
  21 | 
  22 | class EPUBBookLoader(BaseBookLoader):
  23 |     def __init__(
  24 |         self,
  25 |         epub_name,
  26 |         model,
  27 |         key,
  28 |         resume,
  29 |         language,
  30 |         model_api_base=None,
  31 |         is_test=False,
  32 |         test_num=5,
  33 |         prompt_config=None,
  34 |         single_translate=False,
  35 |         context_flag=False,
  36 |         context_paragraph_limit=0,
  37 |         temperature=1.0,
  38 |     ):
  39 |         self.epub_name = epub_name
  40 |         self.new_epub = epub.EpubBook()
  41 |         self.translate_model = model(
  42 |             key,
  43 |             language,
  44 |             api_base=model_api_base,
  45 |             context_flag=context_flag,
  46 |             context_paragraph_limit=context_paragraph_limit,
  47 |             temperature=temperature,
  48 |             **prompt_config_to_kwargs(prompt_config),
  49 |         )
  50 |         self.is_test = is_test
  51 |         self.test_num = test_num
  52 |         self.translate_tags = "p"
  53 |         self.exclude_translate_tags = "sup"
  54 |         self.allow_navigable_strings = False
  55 |         self.accumulated_num = 1
  56 |         self.translation_style = ""
  57 |         self.context_flag = context_flag
  58 |         self.helper = EPUBBookLoaderHelper(
  59 |             self.translate_model,
  60 |             self.accumulated_num,
  61 |             self.translation_style,
  62 |             self.context_flag,
  63 |         )
  64 |         self.retranslate = None
  65 |         self.exclude_filelist = ""
  66 |         self.only_filelist = ""
  67 |         self.single_translate = single_translate
  68 |         self.block_size = -1
  69 |         self.batch_use_flag = False
  70 |         self.batch_flag = False
  71 | 
  72 |         # monkey patch for # 173
  73 |         def _write_items_patch(obj):
  74 |             for item in obj.book.get_items():
  75 |                 if isinstance(item, epub.EpubNcx):
  76 |                     obj.out.writestr(
  77 |                         "%s/%s" % (obj.book.FOLDER_NAME, item.file_name), obj._get_ncx()
  78 |                     )
  79 |                 elif isinstance(item, epub.EpubNav):
  80 |                     obj.out.writestr(
  81 |                         "%s/%s" % (obj.book.FOLDER_NAME, item.file_name),
  82 |                         obj._get_nav(item),
  83 |                     )
  84 |                 elif item.manifest:
  85 |                     obj.out.writestr(
  86 |                         "%s/%s" % (obj.book.FOLDER_NAME, item.file_name), item.content
  87 |                     )
  88 |                 else:
  89 |                     obj.out.writestr("%s" % item.file_name, item.content)
  90 | 
  91 |         def _check_deprecated(obj):
  92 |             pass
  93 | 
  94 |         epub.EpubWriter._write_items = _write_items_patch
  95 |         epub.EpubReader._check_deprecated = _check_deprecated
  96 | 
  97 |         try:
  98 |             self.origin_book = epub.read_epub(self.epub_name)
  99 |         except Exception:
 100 |             # tricky monkey patch for #71 if you don't know why please check the issue and ignore this
 101 |             # when upstream change will TODO fix this
 102 |             def _load_spine(obj):
 103 |                 spine = obj.container.find("{%s}%s" % (epub.NAMESPACES["OPF"], "spine"))
 104 | 
 105 |                 obj.book.spine = [
 106 |                     (t.get("idref"), t.get("linear", "yes")) for t in spine
 107 |                 ]
 108 |                 obj.book.set_direction(spine.get("page-progression-direction", None))
 109 | 
 110 |             epub.EpubReader._load_spine = _load_spine
 111 |             self.origin_book = epub.read_epub(self.epub_name)
 112 | 
 113 |         self.p_to_save = []
 114 |         self.resume = resume
 115 |         self.bin_path = f"{Path(epub_name).parent}/.{Path(epub_name).stem}.temp.bin"
 116 |         if self.resume:
 117 |             self.load_state()
 118 | 
 119 |     @staticmethod
 120 |     def _is_special_text(text):
 121 |         return (
 122 |             text.isdigit()
 123 |             or text.isspace()
 124 |             or is_text_link(text)
 125 |             or all(char in string.punctuation for char in text)
 126 |         )
 127 | 
 128 |     def _make_new_book(self, book):
 129 |         new_book = epub.EpubBook()
 130 |         new_book.metadata = book.metadata
 131 |         new_book.spine = book.spine
 132 |         new_book.toc = book.toc
 133 |         return new_book
 134 | 
 135 |     def _extract_paragraph(self, p):
 136 |         for p_exclude in self.exclude_translate_tags.split(","):
 137 |             # for issue #280
 138 |             if type(p) == NavigableString:
 139 |                 continue
 140 |             for pt in p.find_all(p_exclude):
 141 |                 pt.extract()
 142 |         return p
 143 | 
 144 |     def _process_paragraph(self, p, new_p, index, p_to_save_len):
 145 |         if self.resume and index < p_to_save_len:
 146 |             p.string = self.p_to_save[index]
 147 |         else:
 148 |             t_text = ""
 149 |             if self.batch_flag:
 150 |                 self.translate_model.add_to_batch_translate_queue(index, new_p.text)
 151 |             elif self.batch_use_flag:
 152 |                 t_text = self.translate_model.batch_translate(index)
 153 |             else:
 154 |                 t_text = self.translate_model.translate(new_p.text)
 155 |             if type(p) == NavigableString:
 156 |                 new_p = t_text
 157 |                 self.p_to_save.append(new_p)
 158 |             else:
 159 |                 new_p.string = t_text
 160 |                 self.p_to_save.append(new_p.text)
 161 | 
 162 |         self.helper.insert_trans(
 163 |             p, new_p.string, self.translation_style, self.single_translate
 164 |         )
 165 |         index += 1
 166 | 
 167 |         if index % 20 == 0:
 168 |             self._save_progress()
 169 |         return index
 170 | 
 171 |     def _process_combined_paragraph(self, p_block, index, p_to_save_len):
 172 |         text = []
 173 | 
 174 |         for p in p_block:
 175 |             if self.resume and index < p_to_save_len:
 176 |                 p.string = self.p_to_save[index]
 177 |             else:
 178 |                 p_text = p.text.rstrip()
 179 |                 text.append(p_text)
 180 | 
 181 |             if self.is_test and index >= self.test_num:
 182 |                 break
 183 | 
 184 |             index += 1
 185 | 
 186 |         if len(text) > 0:
 187 |             translated_text = self.translate_model.translate("\n".join(text))
 188 |             translated_text = translated_text.split("\n")
 189 |             text_len = len(translated_text)
 190 | 
 191 |             for i in range(text_len):
 192 |                 t = translated_text[i]
 193 | 
 194 |                 if i >= len(p_block):
 195 |                     p = p_block[-1]
 196 |                 else:
 197 |                     p = p_block[i]
 198 | 
 199 |                 if type(p) == NavigableString:
 200 |                     p = t
 201 |                 else:
 202 |                     p.string = t
 203 | 
 204 |                 self.helper.insert_trans(
 205 |                     p, p.string, self.translation_style, self.single_translate
 206 |                 )
 207 | 
 208 |         self._save_progress()
 209 |         return index
 210 | 
 211 |     def translate_paragraphs_acc(self, p_list, send_num):
 212 |         count = 0
 213 |         wait_p_list = []
 214 |         for i in range(len(p_list)):
 215 |             p = p_list[i]
 216 |             print(f"translating {i}/{len(p_list)}")
 217 |             temp_p = copy(p)
 218 | 
 219 |             for p_exclude in self.exclude_translate_tags.split(","):
 220 |                 # for issue #280
 221 |                 if type(p) == NavigableString:
 222 |                     continue
 223 |                 for pt in temp_p.find_all(p_exclude):
 224 |                     pt.extract()
 225 | 
 226 |             if any(
 227 |                 [not p.text, self._is_special_text(temp_p.text), not_trans(temp_p.text)]
 228 |             ):
 229 |                 if i == len(p_list) - 1:
 230 |                     self.helper.deal_old(wait_p_list, self.single_translate)
 231 |                 continue
 232 |             length = num_tokens_from_text(temp_p.text)
 233 |             if length > send_num:
 234 |                 self.helper.deal_new(p, wait_p_list, self.single_translate)
 235 |                 continue
 236 |             if i == len(p_list) - 1:
 237 |                 if count + length < send_num:
 238 |                     wait_p_list.append(p)
 239 |                     self.helper.deal_old(wait_p_list, self.single_translate)
 240 |                 else:
 241 |                     self.helper.deal_new(p, wait_p_list, self.single_translate)
 242 |                 break
 243 |             if count + length < send_num:
 244 |                 count += length
 245 |                 wait_p_list.append(p)
 246 |             else:
 247 |                 self.helper.deal_old(wait_p_list, self.single_translate)
 248 |                 wait_p_list.append(p)
 249 |                 count = length
 250 | 
 251 |     def get_item(self, book, name):
 252 |         for item in book.get_items():
 253 |             if item.file_name == name:
 254 |                 return item
 255 | 
 256 |     def find_items_containing_string(self, book, search_string):
 257 |         matching_items = []
 258 | 
 259 |         for item in book.get_items_of_type(ITEM_DOCUMENT):
 260 |             content = item.get_content().decode("utf-8")
 261 |             if search_string in content:
 262 |                 matching_items.append(item)
 263 | 
 264 |         return matching_items
 265 | 
 266 |     def retranslate_book(self, index, p_to_save_len, pbar, trans_taglist, retranslate):
 267 |         complete_book_name = retranslate[0]
 268 |         fixname = retranslate[1]
 269 |         fixstart = retranslate[2]
 270 |         fixend = retranslate[3]
 271 | 
 272 |         if fixend == "":
 273 |             fixend = fixstart
 274 | 
 275 |         name_fix = complete_book_name
 276 | 
 277 |         complete_book = epub.read_epub(complete_book_name)
 278 | 
 279 |         if fixname == "":
 280 |             fixname = self.find_items_containing_string(complete_book, fixstart)[
 281 |                 0
 282 |             ].file_name
 283 |             print(f"auto find fixname: {fixname}")
 284 | 
 285 |         new_book = self._make_new_book(complete_book)
 286 | 
 287 |         complete_item = self.get_item(complete_book, fixname)
 288 |         if complete_item is None:
 289 |             return
 290 | 
 291 |         ori_item = self.get_item(self.origin_book, fixname)
 292 |         if ori_item is None:
 293 |             return
 294 | 
 295 |         soup_complete = bs(complete_item.content, "html.parser")
 296 |         soup_ori = bs(ori_item.content, "html.parser")
 297 | 
 298 |         p_list_complete = soup_complete.findAll(trans_taglist)
 299 |         p_list_ori = soup_ori.findAll(trans_taglist)
 300 | 
 301 |         target = None
 302 |         tagl = []
 303 | 
 304 |         # extract from range
 305 |         find_end = False
 306 |         find_start = False
 307 |         for tag in p_list_complete:
 308 |             if find_end:
 309 |                 tagl.append(tag)
 310 |                 break
 311 | 
 312 |             if fixend in tag.text:
 313 |                 find_end = True
 314 |             if fixstart in tag.text:
 315 |                 find_start = True
 316 | 
 317 |             if find_start:
 318 |                 if not target:
 319 |                     target = tag.previous_sibling
 320 |                 tagl.append(tag)
 321 | 
 322 |         for t in tagl:
 323 |             t.extract()
 324 | 
 325 |         flag = False
 326 |         extract_p_list_ori = []
 327 |         for p in p_list_ori:
 328 |             if fixstart in p.text:
 329 |                 flag = True
 330 |             if flag:
 331 |                 extract_p_list_ori.append(p)
 332 |             if fixend in p.text:
 333 |                 break
 334 | 
 335 |         for t in extract_p_list_ori:
 336 |             if target:
 337 |                 target.insert_after(t)
 338 |                 target = t
 339 | 
 340 |         for item in complete_book.get_items():
 341 |             if item.file_name != fixname:
 342 |                 new_book.add_item(item)
 343 |         if soup_complete:
 344 |             complete_item.content = soup_complete.encode()
 345 | 
 346 |         index = self.process_item(
 347 |             complete_item,
 348 |             index,
 349 |             p_to_save_len,
 350 |             pbar,
 351 |             new_book,
 352 |             trans_taglist,
 353 |             fixstart,
 354 |             fixend,
 355 |         )
 356 |         epub.write_epub(f"{name_fix}", new_book, {})
 357 | 
 358 |     def has_nest_child(self, element, trans_taglist):
 359 |         if isinstance(element, Tag):
 360 |             for child in element.children:
 361 |                 if child.name in trans_taglist:
 362 |                     return True
 363 |                 if self.has_nest_child(child, trans_taglist):
 364 |                     return True
 365 |         return False
 366 | 
 367 |     def filter_nest_list(self, p_list, trans_taglist):
 368 |         filtered_list = [p for p in p_list if not self.has_nest_child(p, trans_taglist)]
 369 |         return filtered_list
 370 | 
 371 |     def process_item(
 372 |         self,
 373 |         item,
 374 |         index,
 375 |         p_to_save_len,
 376 |         pbar,
 377 |         new_book,
 378 |         trans_taglist,
 379 |         fixstart=None,
 380 |         fixend=None,
 381 |     ):
 382 |         if self.only_filelist != "" and not item.file_name in self.only_filelist.split(
 383 |             ","
 384 |         ):
 385 |             return index
 386 |         elif self.only_filelist == "" and item.file_name in self.exclude_filelist.split(
 387 |             ","
 388 |         ):
 389 |             new_book.add_item(item)
 390 |             return index
 391 | 
 392 |         if not os.path.exists("log"):
 393 |             os.makedirs("log")
 394 | 
 395 |         soup = bs(item.content, "html.parser")
 396 |         p_list = soup.findAll(trans_taglist)
 397 | 
 398 |         p_list = self.filter_nest_list(p_list, trans_taglist)
 399 | 
 400 |         if self.retranslate:
 401 |             new_p_list = []
 402 | 
 403 |             if fixstart is None or fixend is None:
 404 |                 return
 405 | 
 406 |             start_append = False
 407 |             for p in p_list:
 408 |                 text = p.get_text()
 409 |                 if fixstart in text or fixend in text or start_append:
 410 |                     start_append = True
 411 |                     new_p_list.append(p)
 412 |                 if fixend in text:
 413 |                     p_list = new_p_list
 414 |                     break
 415 | 
 416 |         if self.allow_navigable_strings:
 417 |             p_list.extend(soup.findAll(text=True))
 418 | 
 419 |         send_num = self.accumulated_num
 420 |         if send_num > 1:
 421 |             with open("log/buglog.txt", "a") as f:
 422 |                 print(f"------------- {item.file_name} -------------", file=f)
 423 | 
 424 |             print("------------------------------------------------------")
 425 |             print(f"dealing {item.file_name} ...")
 426 |             self.translate_paragraphs_acc(p_list, send_num)
 427 |         else:
 428 |             is_test_done = self.is_test and index > self.test_num
 429 |             p_block = []
 430 |             block_len = 0
 431 |             for p in p_list:
 432 |                 if is_test_done:
 433 |                     break
 434 |                 if not p.text or self._is_special_text(p.text):
 435 |                     pbar.update(1)
 436 |                     continue
 437 | 
 438 |                 new_p = self._extract_paragraph(copy(p))
 439 |                 if self.single_translate and self.block_size > 0:
 440 |                     p_len = num_tokens_from_text(new_p.text)
 441 |                     block_len += p_len
 442 |                     if block_len > self.block_size:
 443 |                         index = self._process_combined_paragraph(
 444 |                             p_block, index, p_to_save_len
 445 |                         )
 446 |                         p_block = [p]
 447 |                         block_len = p_len
 448 |                         print()
 449 |                     else:
 450 |                         p_block.append(p)
 451 |                 else:
 452 |                     index = self._process_paragraph(p, new_p, index, p_to_save_len)
 453 |                     print()
 454 | 
 455 |                 # pbar.update(delta) not pbar.update(index)?
 456 |                 pbar.update(1)
 457 | 
 458 |                 if self.is_test and index >= self.test_num:
 459 |                     break
 460 |             if self.single_translate and self.block_size > 0 and len(p_block) > 0:
 461 |                 index = self._process_combined_paragraph(p_block, index, p_to_save_len)
 462 | 
 463 |         if soup:
 464 |             item.content = soup.encode()
 465 |         new_book.add_item(item)
 466 | 
 467 |         return index
 468 | 
 469 |     def batch_init_then_wait(self):
 470 |         name, _ = os.path.splitext(self.epub_name)
 471 |         if self.batch_flag or self.batch_use_flag:
 472 |             self.translate_model.batch_init(name)
 473 |             if self.batch_use_flag:
 474 |                 start_time = time.time()
 475 |                 while not self.translate_model.is_completed_batch():
 476 |                     print("Batch translation is not completed yet")
 477 |                     time.sleep(2)
 478 |                     if time.time() - start_time > 300:  # 5 minutes
 479 |                         raise Exception("Batch translation timed out after 5 minutes")
 480 | 
 481 |     def make_bilingual_book(self):
 482 |         self.helper = EPUBBookLoaderHelper(
 483 |             self.translate_model,
 484 |             self.accumulated_num,
 485 |             self.translation_style,
 486 |             self.context_flag,
 487 |         )
 488 |         self.batch_init_then_wait()
 489 |         new_book = self._make_new_book(self.origin_book)
 490 |         all_items = list(self.origin_book.get_items())
 491 |         trans_taglist = self.translate_tags.split(",")
 492 |         all_p_length = sum(
 493 |             (
 494 |                 0
 495 |                 if (
 496 |                     (i.get_type() != ITEM_DOCUMENT)
 497 |                     or (i.file_name in self.exclude_filelist.split(","))
 498 |                     or (
 499 |                         self.only_filelist
 500 |                         and i.file_name not in self.only_filelist.split(",")
 501 |                     )
 502 |                 )
 503 |                 else len(bs(i.content, "html.parser").findAll(trans_taglist))
 504 |             )
 505 |             for i in all_items
 506 |         )
 507 |         all_p_length += self.allow_navigable_strings * sum(
 508 |             (
 509 |                 0
 510 |                 if (
 511 |                     (i.get_type() != ITEM_DOCUMENT)
 512 |                     or (i.file_name in self.exclude_filelist.split(","))
 513 |                     or (
 514 |                         self.only_filelist
 515 |                         and i.file_name not in self.only_filelist.split(",")
 516 |                     )
 517 |                 )
 518 |                 else len(bs(i.content, "html.parser").findAll(text=True))
 519 |             )
 520 |             for i in all_items
 521 |         )
 522 |         pbar = tqdm(total=self.test_num) if self.is_test else tqdm(total=all_p_length)
 523 |         print()
 524 |         index = 0
 525 |         p_to_save_len = len(self.p_to_save)
 526 |         try:
 527 |             if self.retranslate:
 528 |                 self.retranslate_book(
 529 |                     index, p_to_save_len, pbar, trans_taglist, self.retranslate
 530 |                 )
 531 |                 exit(0)
 532 |             # Add the things that don't need to be translated first, so that you can see the img after the interruption
 533 |             for item in self.origin_book.get_items():
 534 |                 if item.get_type() != ITEM_DOCUMENT:
 535 |                     new_book.add_item(item)
 536 | 
 537 |             for item in self.origin_book.get_items_of_type(ITEM_DOCUMENT):
 538 |                 index = self.process_item(
 539 |                     item, index, p_to_save_len, pbar, new_book, trans_taglist
 540 |                 )
 541 | 
 542 |                 if self.accumulated_num > 1:
 543 |                     name, _ = os.path.splitext(self.epub_name)
 544 |                     epub.write_epub(f"{name}_bilingual.epub", new_book, {})
 545 |             name, _ = os.path.splitext(self.epub_name)
 546 |             if self.batch_flag:
 547 |                 self.translate_model.batch()
 548 |             else:
 549 |                 epub.write_epub(f"{name}_bilingual.epub", new_book, {})
 550 |             if self.accumulated_num == 1:
 551 |                 pbar.close()
 552 |         except (KeyboardInterrupt, Exception) as e:
 553 |             print(e)
 554 |             if self.accumulated_num == 1:
 555 |                 print("you can resume it next time")
 556 |                 self._save_progress()
 557 |                 self._save_temp_book()
 558 |             sys.exit(0)
 559 | 
 560 |     def load_state(self):
 561 |         try:
 562 |             with open(self.bin_path, "rb") as f:
 563 |                 self.p_to_save = pickle.load(f)
 564 |         except Exception:
 565 |             raise Exception("can not load resume file")
 566 | 
 567 |     def _save_temp_book(self):
 568 |         # TODO refactor this logic
 569 |         origin_book_temp = epub.read_epub(self.epub_name)
 570 |         new_temp_book = self._make_new_book(origin_book_temp)
 571 |         p_to_save_len = len(self.p_to_save)
 572 |         trans_taglist = self.translate_tags.split(",")
 573 |         index = 0
 574 |         try:
 575 |             for item in origin_book_temp.get_items():
 576 |                 if item.get_type() == ITEM_DOCUMENT:
 577 |                     soup = bs(item.content, "html.parser")
 578 |                     p_list = soup.findAll(trans_taglist)
 579 |                     if self.allow_navigable_strings:
 580 |                         p_list.extend(soup.findAll(text=True))
 581 |                     for p in p_list:
 582 |                         if not p.text or self._is_special_text(p.text):
 583 |                             continue
 584 |                         # TODO banch of p to translate then combine
 585 |                         # PR welcome here
 586 |                         if index < p_to_save_len:
 587 |                             new_p = copy(p)
 588 |                             if type(p) == NavigableString:
 589 |                                 new_p = self.p_to_save[index]
 590 |                             else:
 591 |                                 new_p.string = self.p_to_save[index]
 592 |                             self.helper.insert_trans(
 593 |                                 p,
 594 |                                 new_p.string,
 595 |                                 self.translation_style,
 596 |                                 self.single_translate,
 597 |                             )
 598 |                             index += 1
 599 |                         else:
 600 |                             break
 601 |                     # for save temp book
 602 |                     if soup:
 603 |                         item.content = soup.encode()
 604 |                 new_temp_book.add_item(item)
 605 |             name, _ = os.path.splitext(self.epub_name)
 606 |             epub.write_epub(f"{name}_bilingual_temp.epub", new_temp_book, {})
 607 |         except Exception as e:
 608 |             # TODO handle it
 609 |             print(e)
 610 | 
 611 |     def _save_progress(self):
 612 |         try:
 613 |             with open(self.bin_path, "wb") as f:
 614 |                 pickle.dump(self.p_to_save, f)
 615 |         except Exception:
 616 |             raise Exception("can not save resume file")

```

`/Users/arthrod/Library/CloudStorage/GoogleDrive-arthursrodrigues@gmail.com/My Drive/acode/atemp-drive/bilingual_book_maker/book_maker/__main__.py`:

```py
   1 | from cli import main
   2 | 
   3 | if __name__ == "__main__":
   4 |     main()

```

`/Users/arthrod/Library/CloudStorage/GoogleDrive-arthursrodrigues@gmail.com/My Drive/acode/atemp-drive/bilingual_book_maker/mkdocs.yml`:

```yml
   1 | site_name: bilingual book maker
   2 | theme:
   3 |   name: material
   4 |   features:
   5 |     - navigation.tabs
   6 |     - navigation.tabs.sticky
   7 |     - content.code.copy
   8 | 
   9 | nav: 
  10 |   - Home : index.md
  11 |   - Getting started: 
  12 |     - Installation: installation.md
  13 |     - QuickStart: quickstart.md
  14 |   - Usage:
  15 |     - Model and languages: model_lang.md
  16 |     - Command line options: cmd.md
  17 |     - Translate from different source: book_source.md
  18 |     - Environment setting: env_settings.md
  19 |     - Tweak the prompt: prompt.md
  20 |   - Disclaimer: disclaimer.md
  21 |     

```

`/Users/arthrod/Library/CloudStorage/GoogleDrive-arthursrodrigues@gmail.com/My Drive/acode/atemp-drive/bilingual_book_maker/LICENSE`:

```
   1 | MIT License
   2 | 
   3 | Copyright (c) 2023 yihong
   4 | 
   5 | Permission is hereby granted, free of charge, to any person obtaining a copy
   6 | of this software and associated documentation files (the "Software"), to deal
   7 | in the Software without restriction, including without limitation the rights
   8 | to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
   9 | copies of the Software, and to permit persons to whom the Software is
  10 | furnished to do so, subject to the following conditions:
  11 | 
  12 | The above copyright notice and this permission notice shall be included in all
  13 | copies or substantial portions of the Software.
  14 | 
  15 | THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  16 | IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  17 | FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  18 | AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  19 | LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  20 | OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
  21 | SOFTWARE.

```

`/Users/arthrod/Library/CloudStorage/GoogleDrive-arthursrodrigues@gmail.com/My Drive/acode/atemp-drive/bilingual_book_maker/Dockerfile`:

```
   1 | FROM python:3.10-slim
   2 | 
   3 | RUN apt-get update
   4 | 
   5 | WORKDIR /app
   6 | 
   7 | COPY requirements.txt setup.py .
   8 | 
   9 | RUN pip install -r /app/requirements.txt
  10 | 
  11 | COPY . .
  12 | 
  13 | ENTRYPOINT ["python3", "make_book.py"]

```

`/Users/arthrod/Library/CloudStorage/GoogleDrive-arthursrodrigues@gmail.com/My Drive/acode/atemp-drive/bilingual_book_maker/Makefile`:

```
   1 | SHELL := /bin/bash
   2 | 
   3 | fmt:
   4 | 	@echo "Running formatter ..."
   5 | 	venv/bin/black .
   6 | 
   7 | .PHONY:tests
   8 | tests:
   9 | 	@echo "Running tests ..."
  10 | 	venv/bin/pytest tests/test_integration.py
  11 | 
  12 | serve-docs:
  13 | 	mkdocs serve

```

`/Users/arthrod/Library/CloudStorage/GoogleDrive-arthursrodrigues@gmail.com/My Drive/acode/atemp-drive/bilingual_book_maker/pyproject.toml`:

```toml
   1 | [project]
   2 | name = "bbook-maker"
   3 | description = "The bilingual_book_maker is an AI translation tool that uses ChatGPT to assist users in creating multi-language versions of epub/txt files and books."
   4 | readme = "README.md"
   5 | license = {text = "MIT"}
   6 | dynamic = ["version"]
   7 | requires-python = ">=3.9"
   8 | authors = [
   9 |     { name = "yihong0618", email = "zouzou0208@gmail.com" },
  10 | ]
  11 | classifiers = [
  12 |     "License :: OSI Approved :: MIT License",
  13 |     "Operating System :: OS Independent",
  14 |     "Programming Language :: Python :: 3",
  15 | ]
  16 | dependencies = [
  17 |     "anthropic",
  18 |     "backoff",
  19 |     "bs4",
  20 |     "ebooklib",
  21 |     "google-generativeai",
  22 |     "langdetect",
  23 |     "litellm",
  24 |     "openai>=1.1.1",
  25 |     "PyDeepLX",
  26 |     "requests",
  27 |     "rich",
  28 |     "tiktoken",
  29 |     "tqdm",
  30 |     "groq>=0.5.0",
  31 | ]
  32 | 
  33 | [project.scripts]
  34 | bbook_maker = "book_maker.cli:main"
  35 | 
  36 | [project.urls]
  37 | Homepage = "https://github.com/yihong0618/bilingual_book_maker"
  38 | 
  39 | [tool.pdm]
  40 | plugins = ["pdm-autoexport"]
  41 | [[tool.pdm.autoexport]]
  42 | filename = "requirements.txt"
  43 | without-hashes = true
  44 | [build-system]
  45 | requires = ["pdm-backend>=2.0.0"]
  46 | build-backend = "pdm.backend"
  47 | [tool.pdm.version]
  48 | source = "scm"

```

`/Users/arthrod/Library/CloudStorage/GoogleDrive-arthursrodrigues@gmail.com/My Drive/acode/atemp-drive/bilingual_book_maker/tests/test_integration.py`:

```py
   1 | import os
   2 | import shutil
   3 | import subprocess
   4 | import sys
   5 | from pathlib import Path
   6 | 
   7 | import pytest
   8 | 
   9 | 
  10 | @pytest.fixture()
  11 | def test_book_dir() -> str:
  12 |     """Return test book dir"""
  13 |     # TODO: Can move this to conftest.py if there will be more unittests
  14 |     return str(Path(__file__).parent.parent / "test_books")
  15 | 
  16 | 
  17 | def test_google_translate_epub(test_book_dir, tmpdir):
  18 |     """Test google translate epub"""
  19 |     shutil.copyfile(
  20 |         os.path.join(test_book_dir, "Liber_Esther.epub"),
  21 |         os.path.join(tmpdir, "Liber_Esther.epub"),
  22 |     )
  23 | 
  24 |     subprocess.run(
  25 |         [
  26 |             sys.executable,
  27 |             "make_book.py",
  28 |             "--book_name",
  29 |             os.path.join(tmpdir, "Liber_Esther.epub"),
  30 |             "--test",
  31 |             "--test_num",
  32 |             "20",
  33 |             "--model",
  34 |             "google",
  35 |         ],
  36 |         env=os.environ.copy(),
  37 |     )
  38 | 
  39 |     assert os.path.isfile(os.path.join(tmpdir, "Liber_Esther_bilingual.epub"))
  40 |     assert os.path.getsize(os.path.join(tmpdir, "Liber_Esther_bilingual.epub")) != 0
  41 | 
  42 | 
  43 | def test_deepl_free_translate_epub(test_book_dir, tmpdir):
  44 |     """Test deepl free translate epub"""
  45 |     shutil.copyfile(
  46 |         os.path.join(test_book_dir, "Liber_Esther.epub"),
  47 |         os.path.join(tmpdir, "Liber_Esther.epub"),
  48 |     )
  49 | 
  50 |     subprocess.run(
  51 |         [
  52 |             sys.executable,
  53 |             "make_book.py",
  54 |             "--book_name",
  55 |             os.path.join(tmpdir, "Liber_Esther.epub"),
  56 |             "--test",
  57 |             "--test_num",
  58 |             "20",
  59 |             "--model",
  60 |             "deeplfree",
  61 |         ],
  62 |         env=os.environ.copy(),
  63 |     )
  64 | 
  65 |     assert os.path.isfile(os.path.join(tmpdir, "Liber_Esther_bilingual.epub"))
  66 |     assert os.path.getsize(os.path.join(tmpdir, "Liber_Esther_bilingual.epub")) != 0
  67 | 
  68 | 
  69 | def test_google_translate_epub_cli():
  70 |     pass
  71 | 
  72 | 
  73 | def test_google_translate_txt(test_book_dir, tmpdir):
  74 |     """Test google translate txt"""
  75 |     shutil.copyfile(
  76 |         os.path.join(test_book_dir, "the_little_prince.txt"),
  77 |         os.path.join(tmpdir, "the_little_prince.txt"),
  78 |     )
  79 | 
  80 |     subprocess.run(
  81 |         [
  82 |             sys.executable,
  83 |             "make_book.py",
  84 |             "--book_name",
  85 |             os.path.join(tmpdir, "the_little_prince.txt"),
  86 |             "--test",
  87 |             "--test_num",
  88 |             "20",
  89 |             "--model",
  90 |             "google",
  91 |         ],
  92 |         env=os.environ.copy(),
  93 |     )
  94 |     assert os.path.isfile(os.path.join(tmpdir, "the_little_prince_bilingual.txt"))
  95 |     assert os.path.getsize(os.path.join(tmpdir, "the_little_prince_bilingual.txt")) != 0
  96 | 
  97 | 
  98 | def test_google_translate_txt_batch_size(test_book_dir, tmpdir):
  99 |     """Test google translate txt with batch_size"""
 100 |     shutil.copyfile(
 101 |         os.path.join(test_book_dir, "the_little_prince.txt"),
 102 |         os.path.join(tmpdir, "the_little_prince.txt"),
 103 |     )
 104 | 
 105 |     subprocess.run(
 106 |         [
 107 |             sys.executable,
 108 |             "make_book.py",
 109 |             "--book_name",
 110 |             os.path.join(tmpdir, "the_little_prince.txt"),
 111 |             "--test",
 112 |             "--batch_size",
 113 |             "30",
 114 |             "--test_num",
 115 |             "20",
 116 |             "--model",
 117 |             "google",
 118 |         ],
 119 |         env=os.environ.copy(),
 120 |     )
 121 | 
 122 |     assert os.path.isfile(os.path.join(tmpdir, "the_little_prince_bilingual.txt"))
 123 |     assert os.path.getsize(os.path.join(tmpdir, "the_little_prince_bilingual.txt")) != 0
 124 | 
 125 | 
 126 | @pytest.mark.skipif(
 127 |     not os.environ.get("BBM_CAIYUN_API_KEY"),
 128 |     reason="No BBM_CAIYUN_API_KEY in environment variable.",
 129 | )
 130 | def test_caiyun_translate_txt(test_book_dir, tmpdir):
 131 |     """Test caiyun translate txt"""
 132 |     shutil.copyfile(
 133 |         os.path.join(test_book_dir, "the_little_prince.txt"),
 134 |         os.path.join(tmpdir, "the_little_prince.txt"),
 135 |     )
 136 |     subprocess.run(
 137 |         [
 138 |             sys.executable,
 139 |             "make_book.py",
 140 |             "--book_name",
 141 |             os.path.join(tmpdir, "the_little_prince.txt"),
 142 |             "--test",
 143 |             "--batch_size",
 144 |             "10",
 145 |             "--test_num",
 146 |             "100",
 147 |             "--model",
 148 |             "caiyun",
 149 |         ],
 150 |         env=os.environ.copy(),
 151 |     )
 152 | 
 153 |     assert os.path.isfile(os.path.join(tmpdir, "the_little_prince_bilingual.txt"))
 154 |     assert os.path.getsize(os.path.join(tmpdir, "the_little_prince_bilingual.txt")) != 0
 155 | 
 156 | 
 157 | @pytest.mark.skipif(
 158 |     not os.environ.get("BBM_DEEPL_API_KEY"),
 159 |     reason="No BBM_DEEPL_API_KEY in environment variable.",
 160 | )
 161 | def test_deepl_translate_txt(test_book_dir, tmpdir):
 162 |     shutil.copyfile(
 163 |         os.path.join(test_book_dir, "the_little_prince.txt"),
 164 |         os.path.join(tmpdir, "the_little_prince.txt"),
 165 |     )
 166 | 
 167 |     subprocess.run(
 168 |         [
 169 |             sys.executable,
 170 |             "make_book.py",
 171 |             "--book_name",
 172 |             os.path.join(tmpdir, "the_little_prince.txt"),
 173 |             "--test",
 174 |             "--batch_size",
 175 |             "30",
 176 |             "--test_num",
 177 |             "20",
 178 |             "--model",
 179 |             "deepl",
 180 |         ],
 181 |         env=os.environ.copy(),
 182 |     )
 183 | 
 184 |     assert os.path.isfile(os.path.join(tmpdir, "the_little_prince_bilingual.txt"))
 185 |     assert os.path.getsize(os.path.join(tmpdir, "the_little_prince_bilingual.txt")) != 0
 186 | 
 187 | 
 188 | @pytest.mark.skipif(
 189 |     not os.environ.get("BBM_DEEPL_API_KEY"),
 190 |     reason="No BBM_DEEPL_API_KEY in environment variable.",
 191 | )
 192 | def test_deepl_translate_srt(test_book_dir, tmpdir):
 193 |     shutil.copyfile(
 194 |         os.path.join(test_book_dir, "Lex_Fridman_episode_322.srt"),
 195 |         os.path.join(tmpdir, "Lex_Fridman_episode_322.srt"),
 196 |     )
 197 | 
 198 |     subprocess.run(
 199 |         [
 200 |             sys.executable,
 201 |             "make_book.py",
 202 |             "--book_name",
 203 |             os.path.join(tmpdir, "Lex_Fridman_episode_322.srt"),
 204 |             "--test",
 205 |             "--batch_size",
 206 |             "30",
 207 |             "--test_num",
 208 |             "2",
 209 |             "--model",
 210 |             "deepl",
 211 |         ],
 212 |         env=os.environ.copy(),
 213 |     )
 214 | 
 215 |     assert os.path.isfile(os.path.join(tmpdir, "Lex_Fridman_episode_322_bilingual.srt"))
 216 |     assert (
 217 |         os.path.getsize(os.path.join(tmpdir, "Lex_Fridman_episode_322_bilingual.srt"))
 218 |         != 0
 219 |     )
 220 | 
 221 | 
 222 | @pytest.mark.skipif(
 223 |     not os.environ.get("OPENAI_API_KEY"),
 224 |     reason="No OPENAI_API_KEY in environment variable.",
 225 | )
 226 | def test_openai_translate_epub_zh_hans(test_book_dir, tmpdir):
 227 |     shutil.copyfile(
 228 |         os.path.join(test_book_dir, "lemo.epub"),
 229 |         os.path.join(tmpdir, "lemo.epub"),
 230 |     )
 231 | 
 232 |     subprocess.run(
 233 |         [
 234 |             sys.executable,
 235 |             "make_book.py",
 236 |             "--book_name",
 237 |             os.path.join(tmpdir, "lemo.epub"),
 238 |             "--test",
 239 |             "--test_num",
 240 |             "5",
 241 |             "--language",
 242 |             "zh-hans",
 243 |         ],
 244 |         env=os.environ.copy(),
 245 |     )
 246 |     assert os.path.isfile(os.path.join(tmpdir, "lemo_bilingual.epub"))
 247 |     assert os.path.getsize(os.path.join(tmpdir, "lemo_bilingual.epub")) != 0
 248 | 
 249 | 
 250 | @pytest.mark.skipif(
 251 |     not os.environ.get("OPENAI_API_KEY"),
 252 |     reason="No OPENAI_API_KEY in environment variable.",
 253 | )
 254 | def test_openai_translate_epub_ja_prompt_txt(test_book_dir, tmpdir):
 255 |     shutil.copyfile(
 256 |         os.path.join(test_book_dir, "animal_farm.epub"),
 257 |         os.path.join(tmpdir, "animal_farm.epub"),
 258 |     )
 259 | 
 260 |     subprocess.run(
 261 |         [
 262 |             sys.executable,
 263 |             "make_book.py",
 264 |             "--book_name",
 265 |             os.path.join(tmpdir, "animal_farm.epub"),
 266 |             "--test",
 267 |             "--test_num",
 268 |             "5",
 269 |             "--language",
 270 |             "ja",
 271 |             "--model",
 272 |             "gpt3",
 273 |             "--prompt",
 274 |             "prompt_template_sample.txt",
 275 |         ],
 276 |         env=os.environ.copy(),
 277 |     )
 278 |     assert os.path.isfile(os.path.join(tmpdir, "animal_farm_bilingual.epub"))
 279 |     assert os.path.getsize(os.path.join(tmpdir, "animal_farm_bilingual.epub")) != 0
 280 | 
 281 | 
 282 | @pytest.mark.skipif(
 283 |     not os.environ.get("OPENAI_API_KEY"),
 284 |     reason="No OPENAI_API_KEY in environment variable.",
 285 | )
 286 | def test_openai_translate_epub_ja_prompt_json(test_book_dir, tmpdir):
 287 |     shutil.copyfile(
 288 |         os.path.join(test_book_dir, "animal_farm.epub"),
 289 |         os.path.join(tmpdir, "animal_farm.epub"),
 290 |     )
 291 | 
 292 |     subprocess.run(
 293 |         [
 294 |             sys.executable,
 295 |             "make_book.py",
 296 |             "--book_name",
 297 |             os.path.join(tmpdir, "animal_farm.epub"),
 298 |             "--test",
 299 |             "--test_num",
 300 |             "5",
 301 |             "--language",
 302 |             "ja",
 303 |             "--prompt",
 304 |             "prompt_template_sample.json",
 305 |         ],
 306 |         env=os.environ.copy(),
 307 |     )
 308 |     assert os.path.isfile(os.path.join(tmpdir, "animal_farm_bilingual.epub"))
 309 |     assert os.path.getsize(os.path.join(tmpdir, "animal_farm_bilingual.epub")) != 0
 310 | 
 311 | 
 312 | @pytest.mark.skipif(
 313 |     not os.environ.get("OPENAI_API_KEY"),
 314 |     reason="No OPENAI_API_KEY in environment variable.",
 315 | )
 316 | def test_openai_translate_srt(test_book_dir, tmpdir):
 317 |     shutil.copyfile(
 318 |         os.path.join(test_book_dir, "Lex_Fridman_episode_322.srt"),
 319 |         os.path.join(tmpdir, "Lex_Fridman_episode_322.srt"),
 320 |     )
 321 | 
 322 |     subprocess.run(
 323 |         [
 324 |             sys.executable,
 325 |             "make_book.py",
 326 |             "--book_name",
 327 |             os.path.join(tmpdir, "Lex_Fridman_episode_322.srt"),
 328 |             "--test",
 329 |             "--test_num",
 330 |             "20",
 331 |         ],
 332 |         env=os.environ.copy(),
 333 |     )
 334 |     assert os.path.isfile(os.path.join(tmpdir, "Lex_Fridman_episode_322_bilingual.srt"))
 335 |     assert (
 336 |         os.path.getsize(os.path.join(tmpdir, "Lex_Fridman_episode_322_bilingual.srt"))
 337 |         != 0
 338 |     )

```

`/Users/arthrod/Library/CloudStorage/GoogleDrive-arthursrodrigues@gmail.com/My Drive/acode/atemp-drive/bilingual_book_maker/make_book.py`:

```py
   1 | from book_maker.cli import main
   2 | 
   3 | if __name__ == "__main__":
   4 |     main()

```