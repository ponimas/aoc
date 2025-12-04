#!/usr/bin/env bb


(defn xx [x y]
  (remove #(or (neg? (first %)) (neg? (second %)))
    [[(dec x) y] [(inc x) y] [x (dec y)] [x (inc y)]]))



(let [m (-> (slurp "in/tst.txt")
          (str/split #"\n"))
      s (some
          (fn [n] (when-let [x (-> (nth m n) (str/index-of "S"))]
                    [x n])) (range (count m)))]
  (loop [pos s c 0]

    (recur pos (inc c))))
