#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <string.h>

// كود آلة بسيط لمعمارية ARM64 يقوم فقط بالعودة (Return) بنجاح
unsigned char raw_code[] = { 0xc0, 0x03, 0x5f, 0xd6 }; 

int main() {
    printf("🚀 بدء اختبار تحميل الذاكرة السيادي...\n");

    // 1. حجز صفحة ذاكرة قابلة للكتابة
    void* exec_mem = mmap(NULL, sizeof(raw_code), PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    
    if (exec_mem == MAP_FAILED) {
        perror("❌ فشل حجز الذاكرة");
        return 1;
    }

    // 2. نسخ الكود الخام للذاكرة
    memcpy(exec_mem, raw_code, sizeof(raw_code));

    // 3. تحويل الصلاحية من كتابة إلى تنفيذ (W^X Bypass Attempt)
    if (mprotect(exec_mem, sizeof(raw_code), PROT_READ | PROT_EXEC) == -1) {
        perror("❌ فشل تحويل الصلاحية للتنفيذ");
        return 1;
    }

    // 4. تنفيذ الكود من الذاكرة مباشرة
    void (*func)() = exec_mem;
    func();

    printf("✅ تم التنفيذ بنجاح دون الحاجة لـ ELF Loader التقليدي!\n");
    return 0;
}
