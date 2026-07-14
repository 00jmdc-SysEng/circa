from pathlib import Path

lines = [
    b"%PDF-1.3\n",
    b"1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n",
    b"2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n",
    b"3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>\nendobj\n",
    b"4 0 obj\n<< /Length 82 >>\nstream\nBT\n/F1 24 Tf\n72 720 Td\n(ACN 699 207 264) Tj\n72 680 Td\n(Registration No.) Tj\nET\nendstream\nendobj\n",
    b"5 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\nendobj\n",
]

content = b"".join(lines)

xref_start = len(content)

xref_lines = [
    b"xref\n",
    b"0 6\n",
    b"0000000000 65535 f \n",
]

offset = 0
for part in lines[:-1]:
    xref_lines.append(f"{offset:010} 00000 n \n".encode())
    offset += len(part)

trailer = b"trailer\n<< /Size 6 /Root 1 0 R >>\nstartxref\n"
trailer += str(xref_start).encode() + b"\n%%EOF\n"

pdf_bytes = content + b"".join(xref_lines) + trailer

path = Path("assets/ACN_699_207_264.pdf")
path.write_bytes(pdf_bytes)
print(f"Created PDF ({path}, {len(pdf_bytes)} bytes)")
