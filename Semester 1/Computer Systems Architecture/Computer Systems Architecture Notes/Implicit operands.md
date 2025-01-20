
- **CLD** -> 2 implicit operators: 
**PUSH v** 
- implicit: ESP (destination),
- explicit: source: `v`
`pop eax` - 2 operators
-  2source: ESP - implicit
- destination: `eax` - explicit
`mul reg/mem` (explicit), implicit = `AL/AX/DX:AX` -> `AX/DX:AX/EDX:EAX`