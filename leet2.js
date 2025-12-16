
var merge = function(nums1, m, nums2, n) {
     let p = m-1
     let q = n-1
     let r = m+n -1
    
    while(q >= 0 ){
       if( p >= 0 && nums1[p] > nums2[q]){
         nums1[r] = nums1[p]
        p -=1
    }else{
        nums1[r] = nums2[q]
        q -=1
        
    }
  r -=1
    }



    
    
};