#!/usr/bin/env bb

(defn pairs [l]
  (map vector l (rest l)))

(def data
  (-> (slurp "in/9.txt")
    (str/split #"\n")
    (->> (map #(->>
                 (str/split % #"\s")
                 (map parse-long))))))

;; 1

(defn first-solution [ss]
  (if (apply = ss)
    (last ss)
    (let [xx
          (+ (last ss)
            (first-solution (map (fn [[f s]] (- s f)) (pairs ss))))]
      xx)))

(apply + (for [l data] (first-solution l)))

;; 2

(defn second-solution [ss]
  (println ss)
  (if (apply = ss)
    (first ss)
    (let [xx
          (- (first ss)
            (second-solution (map (fn [[f s]] (- s f)) (pairs ss))))]
      (println xx)
      xx)))

(apply + (for [l data] (second-solution l)))
