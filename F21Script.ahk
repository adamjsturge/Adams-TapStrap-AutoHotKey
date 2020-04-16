#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

#InstallKeybdHook
;#InstallMouseHook ;<--You'll want to use this if you have scripts that use the mouse.
#UseHook On
#SingleInstance force ;only one instance of this script may run at a time!
#MaxHotkeysPerInterval 2000

;;The lines below are optional. Delete them if you need to.
#HotkeyModifierTimeout 60 ; https://autohotkey.com/docs/commands/_HotkeyModifierTimeout.htm
#KeyHistory 200 ; https://autohotkey.com/docs/commands/_KeyHistory.htm ; useful for debugging.
#MenuMaskKey vk07 ;https://autohotkey.com/boards/viewtopic.php?f=76&t=57683
#WinActivateForce ;https://autohotkey.com/docs/commands/_WinActivateForce.htm ;prevent taskbar flashing.
;;The lines above are optional. Delete them if you need to.

F21 & 0::
F21 & a::
F21 & b::
F21 & c::
F21 & d::
F21 & e::
F21 & f::
F21 & g::
F21 & h::
F21 & i::
F21 & j::
F21 & k::
F21 & l::
F21 & m::
F21 & n::
F21 & o::
F21 & p::
F21 & q::
F21 & r::
F21 & s::
F21 & t::
F21 & u::
F21 & v::
F21 & w::
F21 & x::
F21 & y::
F21 & z::
F21 & 1::
F21 & 2::
F21 & 3::
F21 & 4::
F21 & 5::
F21 & 6::
F21 & 7::
F21 & 8::
F21 & 9::
tooltip, you pressed the function key %A_thishotkey% on Tap
Return