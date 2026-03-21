import re

def sort_timo_matrix():
    file_path = 'index.html'
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # تحديد مكان مصفوفة البيانات (knowledgeBase أو narsaLaw)
        matrix_match = re.search(r'const (knowledgeBase|narsaLaw) = \{(.*?)\};', content, re.DOTALL)
        
        if matrix_match:
            matrix_name = matrix_match.group(1)
            matrix_body = matrix_match.group(2)
            
            # تقسيم الأسطر وترتيبها أبجدياً
            items = [item.strip() for item in matrix_body.split(',') if item.strip()]
            items.sort()
            
            new_matrix_body = ',\n    ' + ',\n    '.join(items)
            new_content = content.replace(matrix_body, new_matrix_body)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ تم ترتيب {matrix_name} بنجاح داخل index.html")
        else:
            print("❌ لم يتم العثور على مصفوفة البيانات")
            
    except Exception as e:
        print(f"⚠️ خطأ: {e}")

if __name__ == "__main__":
    sort_timo_matrix()
