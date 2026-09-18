function isAnagram(s: string, t: string): boolean {
    let sCharCount = new Map<string, number>(); 
    let tCharCount = new Map<string, number>();

    for (const char of s){
        if (sCharCount.has(char))
            sCharCount.set(char, sCharCount.get(char) + 1);
        else 
            sCharCount.set(char, 1);
    }

    for (const char of t){
        if (tCharCount.has(char))
            tCharCount.set(char, tCharCount.get(char)+1);
        else 
            tCharCount.set(char,1);
    }

    if (tCharCount.size != sCharCount.size)
        return false;
    for (const [key, value] of tCharCount){
        if (!sCharCount.has(key) || sCharCount.get(key) != value)
            return false;
