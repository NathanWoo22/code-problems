function containsDuplicate(nums: number[]): boolean {
    const numCount = new Map<number, number>(); 
    for (const num of nums){
        if (numCount.has(num))
            return true;
        numCount.set(num, 1);
    }
    return false;
};

console.log(containsDuplicate([1, 2, 3, 4]));
console.log(containsDuplicate([1, 2, 3, 1]));
