#!/usr/bin/env bb

(defn pairs [l]
  (map vector l (rest l)))

(defn first-solution [ss]
  (if (apply = ss)
    (last ss)
    (let [xx
          (+ (last ss)
            (x (map (fn [[f s]] (- s f)) (pairs ss))))]
      xx)))


(let [data (-> (slurp "in/9.txt")
             (str/split #"\n")
             (->> (map #(->>
                          (str/split % #"\s")
                          (map parse-long)))))]
  (apply + (for [l data] (first-solution l))))
