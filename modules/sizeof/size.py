replacements = [
    (b"idata", b".1_"),
    (b"\xFF\xFF\xFF", b".2_"),
    (b"\x00\x00\x00\x00\x00", b".3_"),
    (b"ZZZZZZ", b".4_"),
    (b"This program cannot be run in DOS mode.", b".5_"),
    (b"\x70\x6F\x8D", b".6_"),
    (b"__Display", b".7_"),
    (b"<update>", b".8_"),
    (b"\xC1\xC1\xC1\xFF\xC1\xC1\xC1\xFF", b".9_"),
    (b"\xC4\xC4\xC4\xFF\xC4\xC4\xC4\xFF", b".0_"),
    (b"\xC0\xC0\xC0\xFF\xC0\xC0\xC0\xFF", b".$^"),
    (b"\xCC\xCC\xCC\xCC\xCC\xCC", b".!d^"),
    (b"System", b".@_"),
    (b"kwsc", b".{_"),
    (b"$char_traits", b".c!t_"),
    (b"tttttt", b".\xC0_"),
    (b"cccccc", b".\xC1_"),
    (b"gggggg", b".\xC2_"),
    (b"\x90\x90\x90\x90\x90\x90", b".\xC3_"),
    (b"\x80\x80\x80\x80\x80\x80", b".\xC4_"),
    (b"\xf6\xc4\x01t\x05", b".\xC5_"),
    (b"\xff\xf5\xf5\xf5\xff\xf5", b".\xC6_"),
    (b"\xf5\xff\xf5\xf5\xf5\xff", b".\xC7_"),
    (b"\xcc\xcc\xcc\xcc\xcc\xcc", b".\xC8_"),
]